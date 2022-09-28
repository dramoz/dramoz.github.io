# =========================================================================================
#  GitHub.io Pages with Jekyll+Chirpy
#  Copyright (c) 2022.  Danilo Ramos
#  All rights reserved.
#  Licensed under the MIT license (https://choosealicense.com/licenses/mit/)
# =========================================================================================
# https://www.gnu.org/software/make/manual/html_node/index.html#SEC_Contents
# https://pages.github.com/
# https://docs.github.com/en/pages/setting-up-a-github-pages-site-with-jekyll
# =========================================================================================
# Target and directories

# Makefile tasks for Jekyll
# --------------------------------------------------------------------------------
# Env. Setup
VENV_NAME ?= dev
VEVN_DIR  ?= ~/.virtualenvs
VENV_PATH = $(VEVN_DIR)/$(VENV_NAME)
VENV = $(VENV_PATH)/bin/activate
VENV_EXISTS = $(or $(and $(wildcard $(VENV)),1),0)

define python_mk
  @. $(VENV)
  @python -c "from Makefile import $(1); $(1)($(2))"
endef

# --------------------------------------------------------------------------------
# Jekyll Server
.PHONY: run_jekyll
run_jekyll:
	$(call python_mk,run_process,'jekyll serve --watch --drafts --incremental')
	@sleep 1
	$(call python_mk,run_process,'firefox --new-tab http://127.0.0.1:4000/')

.PHONY: reload_jekyll
reload_jekyll: kill_jekyll clean
	$(call python_mk,reload_process,'jekyll serve --watch --drafts --incremental')

.PHONY: open_local_web
open_local_web:
	$(call python_mk,run_process,'firefox --new-tab http://127.0.0.1:4000/')

.PHONY: terminate_jekyll
terminate_jekyll:
	$(call python_mk,terminate_process,'jekyll')

.PHONY: kill_jekyll
kill_jekyll:
	$(call python_mk,kill_process,'jekyll')

# --------------------------------------------------------------------------------
# Posts
.PHONY: new_draft_post
.ONESHELL:
new_draft_post:
	@read -p "Draft title: " TITLE;
	@jekyll draft $$TITLE

# --------------------------------------------------------------------------------
# Tools setup
.ONESHELL:
$(VENV): requirements.txt
ifeq ("$(wildcard $(VENV))","")
	@echo "Creating python virtual environment: $(VENV_PATH)"
	@mkdir -p $(VEVN_DIR)
	@python3 -m venv $(VENV_PATH)
endif
	@. $(VENV)
	@pip install -r requirements.txt

.PHONY: tools_setup
.ONESHELL:
tools_setup:
# HDL convertor requirements
	sudo apt install -y build-essential uuid-dev cmake default-jre python3 python3-dev python3-pip libantlr4-runtime-dev antlr4 ninja-build
	$(MAKE) $(VENV)
#ifeq (, $(shell which verilator))
#	mkdir -p ~/repos
#	cd ~/repos
#	
#endif

# --------------------------------------------------------------------------------
.PHONY: clean
clean::
	jekyll clean
	rm -rf __pycache__
