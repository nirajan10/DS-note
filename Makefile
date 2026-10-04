# Targets for the DSC 481 notes site.
#   make install   create .venv and install everything
#   make serve     live-preview the site at http://127.0.0.1:8000
#   make build     strict build into ./site (only the topics released in mkdocs.yml)
#   make build-all strict build of the WHOLE course into ./site-all (all topics released)
#   make figures   rebuild every PNG in docs/assets/img (light and dark)
#   make data      rebuild the small CSV / JSON / XLSX files in docs/assets/data
#   make examples  re-run every Python example and rewrite its Output block
#   make check     examples match real output + strict builds (all topics, and as released) + HTML checks

VENV   ?= .venv
PY     := $(VENV)/bin/python
MKDOCS := $(VENV)/bin/mkdocs
export NO_MKDOCS_2_WARNING := true

.PHONY: install serve build build-all figures data examples check

install:
	python3 -m venv $(VENV)
	$(PY) -m pip install --upgrade pip
	$(PY) -m pip install -r requirements.txt

serve:
	NO_MKDOCS_2_WARNING=true $(MKDOCS) serve

build:
	NO_MKDOCS_2_WARNING=true $(MKDOCS) build --strict -d site

build-all:
	NO_MKDOCS_2_WARNING=true $(MKDOCS) build --strict -f mkdocs-all.yml -d site-all

figures:
	$(PY) scripts/make_figures.py

data:
	$(PY) scripts/make_data.py

examples:
	$(PY) scripts/run_examples.py --write

check:
	$(PY) scripts/run_examples.py --check
	NO_MKDOCS_2_WARNING=true $(MKDOCS) build --strict -f mkdocs-all.yml -d /tmp/sitecheck
	NO_MKDOCS_2_WARNING=true $(MKDOCS) build --strict -d /tmp/sitecheck-released
	$(PY) scripts/verify_site.py /tmp/sitecheck
