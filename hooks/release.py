"""Release control: only pages listed in `nav` are published.

MkDocs normally builds every .md file in docs/, even when it is missing from the nav (it stays
reachable by URL and shows up in search). This hook makes the nav the single switch:

  * a page that is NOT in the nav is not built at all (no HTML, no search entry);
  * a link from a published page to an unpublished one is turned into plain text, so nothing
    breaks and nothing leaks.

To release a topic, uncomment its lines in mkdocs.yml. To hide it again, comment them out.
"""
import posixpath
import re

LINK = re.compile(r"\[([^\]]+)\]\(([^)\s#]+\.md)(#[^)\s]*)?\)")


def _nav_pages(nav):
    found = set()
    if isinstance(nav, str):
        found.add(nav)
    elif isinstance(nav, dict):
        for value in nav.values():
            found |= _nav_pages(value)
    elif isinstance(nav, list):
        for item in nav:
            found |= _nav_pages(item)
    return found


def on_files(files, config):
    nav = config.get("nav")
    if not nav:
        return files
    released = _nav_pages(nav)
    config["_released_pages"] = released
    for f in list(files.documentation_pages()):
        if f.src_uri not in released:
            files.remove(f)
    return files


def on_page_markdown(markdown, page, config, files):
    released = config.get("_released_pages")
    if released is None:
        return markdown
    here = posixpath.dirname(page.file.src_uri)

    def strip(match):
        target = posixpath.normpath(posixpath.join(here, match.group(2)))
        return match.group(0) if target in released else match.group(1)

    return LINK.sub(strip, markdown)
