"""Shared helpers: find fenced code blocks in the notes and run Python examples.

Authoring conventions (full details in AUTHORING.md)
----------------------------------------------------
A fenced ```python block is an example. Write only the code; run

    python scripts/run_examples.py --write

and the real output is inserted right after it as a block titled "Output".

Directives go in an HTML comment on the line(s) just above the code block:

    <!-- stdin: Asha | 78 -->     values typed in for input() calls, in order
    <!-- error -->                the example is meant to fail; show its traceback
    <!-- continue -->             run this block after the previous example, in the
                                  same session (variables are kept); only the NEW
                                  output is shown
    <!-- file: helpers.py -->     this block is a file saved next to the later
                                  examples on the page; it is not run itself
    <!-- figure: u08-hist -->     this block draws a figure; make_figures.py saves it
                                  as docs/assets/img/u08-hist.png (and -dark.png)
    <!-- plotly: u10-scatter -->  this block builds a Plotly figure and calls fig.show();
                                  make_figures.py saves docs/assets/plotly/u10-scatter.html
                                  (and -dark.html) so the page can embed it
    <!-- answer -->               run this block, but show its output in a LATER Output
                                  block (inside a collapsible answer), not right below it
    <!-- serve: 8 -->             a web server (Dash app): run it for 8 seconds, stop it, and
                                  show what it printed on start-up
    <!-- script: app.py -->      run the block under this file name (shows in tracebacks and as
                                  the Flask app name); default is example.py
    <!-- online -->               needs the internet; only run with --online
    <!-- no-run -->               never run (servers, GUI windows); say why in the text
"""
import hashlib
import os
import re
import signal
import shutil
import subprocess
import sys
import tempfile
from dataclasses import dataclass, field
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
DATA = DOCS / "assets" / "data"
IMG = DOCS / "assets" / "img"

FENCE_RE = re.compile(r"^(?P<indent>[ \t]*)(?P<fence>`{3,}|~{3,})[ \t]*(?P<info>.*?)[ \t]*$")
COMMENT_RE = re.compile(r"^\s*<!--\s*(?P<body>.*?)\s*-->\s*$")
OUTPUT_INFO_RE = re.compile(r'title\s*=\s*"Output"')
KNOWN_FLAGS = {"error", "continue", "online", "no-run", "answer"}
KNOWN_KEYS = {"stdin", "file", "figure", "plotly", "serve", "script"}


@dataclass
class Block:
    path: Path
    start: int          # line index of the opening fence
    end: int            # line index of the closing fence
    indent: str
    fence: str
    info: str
    code: str           # dedented source text
    directives: dict = field(default_factory=dict)
    # filled in by resolve():
    kind: str = "other"         # "run", "file", "skip", "output", "other"
    full_code: str = ""         # code of the whole chain (for `continue`)
    full_stdin: tuple = ()
    prev: "Block | None" = None  # previous block in a `continue` chain
    files: dict = field(default_factory=dict)   # file blocks visible to this one
    output: "Block | None" = None               # the Output block after it, if any

    @property
    def lang(self):
        return self.info.split()[0].strip("{.}") if self.info else ""

    @property
    def line(self):
        return self.start + 1  # 1-based, for messages


def parse_blocks(path):
    """Return (lines, blocks) for one markdown file."""
    lines = Path(path).read_text(encoding="utf-8").split("\n")
    blocks, i = [], 0
    while i < len(lines):
        m = FENCE_RE.match(lines[i])
        if not m:
            i += 1
            continue
        indent, fence, info = m["indent"], m["fence"], m["info"]
        j = i + 1
        while j < len(lines):
            c = FENCE_RE.match(lines[j])
            if c and c["fence"][0] == fence[0] and len(c["fence"]) >= len(fence) and not c["info"]:
                break
            j += 1
        if j >= len(lines):
            raise ValueError(f"{path}:{i + 1}: code fence is never closed")
        body = []
        for k, ln in enumerate(lines[i + 1:j], start=i + 2):
            if ln.startswith(indent):
                body.append(ln[len(indent):])
            elif not ln.strip():
                body.append("")
            else:
                raise ValueError(f"{path}:{k}: this line is inside a code fence that is indented "
                                 f"{len(indent)} spaces, but the line is not; indent it to match")
        blk = Block(Path(path), i, j, indent, fence, info, "\n".join(body))
        blk.directives = read_directives(lines, i)
        blocks.append(blk)
        i = j + 1
    return lines, blocks


def read_directives(lines, fence_index):
    """Collect directives from the comment line(s) just above a fence."""
    found, k = {}, fence_index - 1
    while k >= 0 and not lines[k].strip():
        k -= 1
    while k >= 0:
        m = COMMENT_RE.match(lines[k])
        if not m:
            break
        for part in m["body"].split(";"):
            part = part.strip()
            if ":" in part:
                key, val = part.split(":", 1)
                key = key.strip()
                if key in KNOWN_KEYS:
                    found[key] = val.strip()
            elif part in KNOWN_FLAGS:
                found[part] = True
        k -= 1
    return found


def resolve(blocks, lines):
    """Classify blocks, link Output blocks and `continue` chains."""
    files, last_run = {}, None
    for idx, b in enumerate(blocks):
        if b.lang != "python":
            if OUTPUT_INFO_RE.search(b.info):
                b.kind = "output"
            continue
        d = b.directives
        if "file" in d:
            b.kind = "file"
            files[d["file"]] = b.code
            continue
        if d.get("no-run"):
            b.kind = "skip"
            continue
        b.kind = "run"
        b.files = dict(files)
        stdin = tuple(s.strip() for s in d["stdin"].split("|")) if "stdin" in d else ()
        if d.get("continue"):
            if last_run is None:
                raise ValueError(f"{b.path}:{b.line}: `continue` has nothing to continue")
            b.prev = last_run
            b.full_code = last_run.full_code + "\n" + b.code
            b.full_stdin = last_run.full_stdin + stdin
        else:
            b.full_code, b.full_stdin = b.code, stdin
        last_run = b
        if d.get("answer"):
            # the Output block lives later (in the collapsible answer); take the next one,
            # as long as no other runnable example comes first
            for later in blocks[idx + 1:]:
                if later.lang == "python" and "file" not in later.directives:
                    break
                if OUTPUT_INFO_RE.search(later.info) and later.lang != "python":
                    b.output = later
                    break
            continue
        # otherwise the Output block must follow the code with nothing but blank lines between
        nxt = blocks[idx + 1] if idx + 1 < len(blocks) else None
        if nxt is not None and OUTPUT_INFO_RE.search(nxt.info) and nxt.lang != "python":
            if not "\n".join(lines[b.end + 1:nxt.start]).strip():
                b.output = nxt
    return blocks


def load(path):
    lines, blocks = parse_blocks(path)
    return lines, resolve(blocks, lines)


def markdown_files(paths=None):
    if paths:
        return [Path(p).resolve() for p in paths]
    return sorted(DOCS.rglob("*.md"))


# --- running code ---------------------------------------------------------------

SHIM = r'''
import builtins, os, runpy, sys, traceback

_values = iter(__STDIN__)


def _input(prompt=""):
    try:
        value = next(_values)
    except StopIteration:
        raise EOFError("this example ran out of typed-in values (add `stdin:`)")
    print(f"{prompt}{value}")  # echo the typed value, like a terminal does
    return value


builtins.input = _input

_code = open("__SCRIPT__", encoding="utf-8").read()
if "plotly" in _code:
    import plotly.basedatatypes as _bdt
    _bdt.BaseFigure.show = lambda self, *a, **k: None  # no browser window in a test run
if any(k in _code for k in ("matplotlib", "seaborn", "pyplot", "sns.")):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    plt.show = lambda *a, **k: None

try:
    runpy.run_path("__SCRIPT__", run_name="__main__")
except SystemExit:
    raise
except BaseException:
    etype, err, tb = sys.exc_info()
    here = os.getcwd()
    # keep only the student's own files (in the working folder), not library or runner frames
    frames = [f for f in traceback.extract_tb(tb)
              if os.path.isfile(f.filename) and os.path.abspath(f.filename).startswith(here + os.sep)
              and os.path.basename(f.filename) != "_shim.py"]
    out = []
    if frames:
        out.append("Traceback (most recent call last):\n")
        out.extend(traceback.format_list(frames))
    out.extend(traceback.format_exception_only(etype, err))
    sys.stdout.write("".join(out))
    sys.exit(1)
'''


def _env():
    env = dict(os.environ)
    env.update(
        USER="asha", LOGNAME="asha",   # what getpass.getuser() reports in the examples
        PYTHONUNBUFFERED="1", PYTHONHASHSEED="0", PYTHONIOENCODING="utf-8",
        MPLBACKEND="Agg", COLUMNS="80", LC_ALL="C.UTF-8", NO_COLOR="1",
        MPLCONFIGDIR=str(Path(tempfile.gettempdir()) / "mplconfig-notes"),
    )
    return env


def workdir_with_data(files=None):
    """A fresh temp folder holding copies of the practice data and any `file:` blocks."""
    tmp = Path(tempfile.mkdtemp(prefix="notes-example-"))
    for f in DATA.iterdir():
        if f.is_file():
            shutil.copy(f, tmp / f.name)
    for name, text in (files or {}).items():
        (tmp / name).write_text(text + "\n", encoding="utf-8")
    return tmp


_cache = {}


def run_code(code, files=None, stdin=(), timeout=240, serve=None, script="example.py"):
    """Run code in a clean folder; return (ok, output). Output merges stdout and stderr.

    serve=N: the code starts a web server; stop it after N seconds and keep what it printed.
    """
    key = hashlib.sha1(repr((code, sorted((files or {}).items()), stdin, serve, script)).encode()).hexdigest()
    if key in _cache:
        return _cache[key]
    tmp = workdir_with_data(files)
    try:
        (tmp / script).write_text(code + "\n", encoding="utf-8")
        shim = SHIM.replace("__STDIN__", repr(list(stdin))).replace("__SCRIPT__", script)
        (tmp / "_shim.py").write_text(shim, encoding="utf-8")
        if serve:
            proc = subprocess.Popen(
                [sys.executable, "_shim.py"], cwd=tmp, env=_env(), stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT, text=True, stdin=subprocess.DEVNULL, start_new_session=True,
            )
            try:
                out, _ = proc.communicate(timeout=float(serve))
                ok = proc.returncode == 0          # it stopped by itself
            except subprocess.TimeoutExpired:
                os.killpg(proc.pid, signal.SIGTERM)  # also stops Dash's auto-reload child
                out, _ = proc.communicate(timeout=20)
                ok = "Traceback" not in out
            out = out.replace(sys.executable, f"{tmp}/.venv/bin/python")
            result = (ok, out.replace(str(tmp), "/home/student/project").rstrip("\n"))
            _cache[key] = result
            return result
        try:
            p = subprocess.run(
                [sys.executable, "_shim.py"], cwd=tmp, env=_env(), capture_output=True,
                text=True, timeout=timeout, stdin=subprocess.DEVNULL,
            )
            out = (p.stdout + p.stderr).replace(sys.executable, f"{tmp}/.venv/bin/python")
            out = out.replace(str(tmp), "/home/student/project")
            result = (p.returncode == 0, out.rstrip("\n"))
        except subprocess.TimeoutExpired:
            result = (False, f"TIMEOUT after {timeout}s")
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    _cache[key] = result
    return result


def _script(block):
    return block.directives.get("script", "example.py")


def expected_output(block):
    """Run the block (and its chain); return (ok, text_to_show)."""
    ok, full = run_code(block.full_code, block.files, block.full_stdin,
                        serve=block.directives.get("serve"), script=_script(block))
    if block.prev is None or not ok:
        return ok, full
    ok0, before = run_code(block.prev.full_code, block.prev.files, block.prev.full_stdin, script=_script(block.prev))
    if not ok0:
        return False, "the earlier block of this `continue` chain failed:\n" + before
    if not full.startswith(before):
        return False, "output of the earlier blocks changed when this block was added"
    return True, full[len(before):].strip("\n")
