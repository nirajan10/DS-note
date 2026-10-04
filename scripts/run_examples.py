"""Run every Python example in the notes and keep the printed output real.

    python scripts/run_examples.py                 check: re-run all examples, report any mismatch
    python scripts/run_examples.py --write         insert / refresh the Output blocks from real runs
    python scripts/run_examples.py docs/unit-03-control.md   limit to some files
    python scripts/run_examples.py --online        also run the examples marked <!-- online -->

Exit code is 1 if any example fails, any Output block is out of date, or an
example prints something that has no Output block.
"""
import argparse
import re
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import mdblocks as mb  # noqa: E402

WARN_RE = re.compile(r"\b\w*Warning\b")


def plan(path, online):
    """Return (lines, jobs); each job is a runnable block."""
    lines, blocks = mb.load(path)
    jobs = []
    for b in blocks:
        if b.kind == "output" and not any(x.output is b for x in blocks):
            print(f"  ERROR {path.name}:{b.line}: Output block with no Python example above it")
            jobs.append(("orphan", b))
        if b.kind != "run":
            continue
        if b.directives.get("online") and not online:
            jobs.append(("online-skipped", b))
        else:
            jobs.append(("run", b))
    return lines, jobs


def render_output(block, text):
    ind, fence = block.indent, "```"
    body = [(ind + ln) if ln else "" for ln in text.split("\n")]
    return [open_line(block), *body, f"{ind}{fence}"]


def open_line(block):
    """The attr_list form gives the block class="output", which the CSS styles."""
    return block.indent + '```{ .text .output title="Output" }'


def process(path, write, online, pool):
    lines, jobs = plan(path, online)
    runnable = [b for kind, b in jobs if kind == "run"]
    results = dict(zip((id(b) for b in runnable), pool.map(mb.expected_output, runnable)))
    problems, edits = 0, []   # edits: (start, end_inclusive, new_lines)
    counts = {"run": 0, "ok": 0, "online-skipped": 0, "no-output": 0}
    for kind, b in jobs:
        if kind == "orphan":
            problems += 1
            continue
        if kind == "online-skipped":
            counts["online-skipped"] += 1
            continue
        counts["run"] += 1
        ok, text = results[id(b)]
        expect_error = bool(b.directives.get("error"))
        where = f"{path.name}:{b.line}"
        if not ok and not expect_error:
            print(f"  FAIL  {where}: example raised an error\n" + indent(text))
            problems += 1
            continue
        if ok and expect_error:
            print(f"  FAIL  {where}: marked <!-- error --> but it ran without error")
            problems += 1
            continue
        if WARN_RE.search(text):
            print(f"  FAIL  {where}: output contains a warning; fix the example\n" + indent(text))
            problems += 1
            continue
        if b.directives.get("answer") and b.output is None:
            print(f"  FAIL  {where}: <!-- answer --> needs an Output block later in the answer "
                  "(add an empty one: ```{ .text .output title=\"Output\" }```)")
            problems += 1
            continue
        existing = None
        if b.output is not None:
            existing = "\n".join(
                ln[len(b.output.indent):] if ln.startswith(b.output.indent) else ln
                for ln in lines[b.output.start + 1:b.output.end]
            ).rstrip("\n")
        if not text.strip():
            counts["no-output"] += 1
            if existing is not None:
                print(f"  {'REMOVE' if write else 'STALE'} {where}: example prints nothing but has an Output block")
                if write:
                    edits.append((b.output.start - 1 if lines[b.output.start - 1] == "" else b.output.start,
                                  b.output.end, []))
                else:
                    problems += 1
            continue
        if existing == text and lines[b.output.start] == open_line(b.output):
            counts["ok"] += 1
            continue
        if write:
            new = render_output(b.output if b.output is not None else b, text)
            if b.output is not None:
                edits.append((b.output.start, b.output.end, new))
            else:
                edits.append((b.end + 1, b.end, ["", *new]))   # pure insertion after the code block
            counts["ok"] += 1
        else:
            what = "missing Output block" if existing is None else "Output block is out of date"
            print(f"  STALE {where}: {what}")
            problems += 1
    if write and edits:
        for start, end, new in sorted(edits, key=lambda e: -e[0]):
            lines[start:end + 1] = new
        path.write_text("\n".join(lines), encoding="utf-8")
        print(f"  wrote {len(edits)} output block(s) in {path.name}")
    return counts, problems


def indent(text, pad="      "):
    return "\n".join(pad + ln for ln in text.split("\n")[-12:])


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("files", nargs="*", help="markdown files (default: every page in docs/)")
    ap.add_argument("--write", action="store_true", help="insert / refresh Output blocks")
    ap.add_argument("--check", action="store_true", help="only check (this is the default)")
    ap.add_argument("--online", action="store_true", help="also run examples marked <!-- online -->")
    ap.add_argument("-j", type=int, default=6, help="examples to run at the same time")
    args = ap.parse_args()

    total, bad = {}, 0
    with ThreadPoolExecutor(max_workers=args.j) as pool:
        for path in mb.markdown_files(args.files):
            print(path.relative_to(mb.ROOT) if path.is_relative_to(mb.ROOT) else path)
            counts, problems = process(path, args.write, args.online, pool)
            bad += problems
            for k, v in counts.items():
                total[k] = total.get(k, 0) + v
            print(f"  {counts['run']} run, {counts['ok']} with matching output, "
                  f"{counts['no-output']} print nothing, {counts['online-skipped']} online skipped")
    print(f"\nTOTAL: {total.get('run', 0)} examples run, {total.get('ok', 0)} outputs match, "
          f"{total.get('online-skipped', 0)} online skipped, {bad} problem(s)")
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
