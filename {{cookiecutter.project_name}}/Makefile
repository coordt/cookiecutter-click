.DEFAULT_GOAL := help
.PHONY:
PROJ_SLUG = {{cookiecutter.package_name}}
CLI_NAME = {{cookiecutter.cli_name}}

define BROWSER_PYSCRIPT
import os, webbrowser, sys
try:
	from urllib import pathname2url
except:
	from urllib.request import pathname2url

webbrowser.open("file://" + pathname2url(os.path.abspath(sys.argv[1])))
endef
export BROWSER_PYSCRIPT
BROWSER := python -c "$$BROWSER_PYSCRIPT"

define ENSURE_MASTER_BRANCH_SCRIPT
BRANCH=$$(git rev-parse --abbrev-ref HEAD)
if [[ "$$BRANCH" != "master" ]]; then
  echo 'You can only release new versions when on the master branch.';
  exit 1;
fi
endef
export ENSURE_MASTER_BRANCH_SCRIPT
ENSURE_MASTER_BRANCH := bash -c "$$ENSURE_MASTER_BRANCH_SCRIPT"

help:
	@grep '^[a-zA-Z]' $(MAKEFILE_LIST) | sort | awk -F ':.*?## ' 'NF==2 {printf "\033[36m  %-25s\033[0m %s\n", $$1, $$2}'

clean : ## remove build artifacts
	rm -rf dist
	rm -rf docs/build
	rm -rf *.egg-info
	coverage erase

lint: ## check style with flake8
	flake8 $(PROJ_SLUG) tests

test: lint
	py.test --cov-report term --cov=$(PROJ_SLUG) tests/

run:
	$(CLI_NAME) run

submit:
	$(CLI_NAME) submit

test: ## run tests quickly with the default Python
	[ ! -e testserver.log ] || rm testserver.log
	py.test

test-all: ## run tests on every Python version with tox
	tox

coverage: ## check code coverage quickly with the default Python
	coverage run --source $(PROJ_SLUG) -m pytest
	coverage report -m
	coverage html
	$(BROWSER) htmlcov/index.html

docs: ## generate Sphinx HTML documentation, including API docs
	rm -f docs/api/$(PROJ_SLUG)*.rst
	sphinx-apidoc -o docs/api $(PROJ_SLUG)
	$(MAKE) -C docs clean
	$(MAKE) -C docs html

package: clean docs
	rm -rf dist/
	python setup.py bdist_wheel

publish: package
	twine upload dist/*

venv: ## create a virtual environment
	python3 -m venv venv
	source venv/bin/activate && pip install pip --upgrade --index-url=https://pypi.org/simple

install: ## install requirements for running the app
	pip install -r requirements/prod.txt

install-dev: ## install all requirements for development
	pip install -r requirements/dev.txt

install-test: ## install all requirements for running tests
	pip install -r requirements/prod.txt
	pip install -r requirements/test.txt

release-patch:  ## Release a new version: 1.1.1 -> 1.1.2
	$(ENSURE_MASTER_BRANCH)
	git fetch -p --all
	gitchangelog
ifdef EDITOR
	$(EDITOR) CHANGELOG.md
endif
	bump2version patch --allow-dirty
	git push
	git push --tags

release-minor:  ## Release a new version: 1.1.1 -> 1.2.0
	$(ENSURE_MASTER_BRANCH)
	git fetch -p --all
	gitchangelog
ifdef EDITOR
	$(EDITOR) CHANGELOG.md
endif
	bump2version minor --allow-dirty
	git push
	git push --tags

release-major:  ## Release a new version: 1.1.1 -> 2.0.0
	$(ENSURE_MASTER_BRANCH)
	git fetch -p --all
	gitchangelog
ifdef EDITOR
	$(EDITOR) CHANGELOG.md
endif
	bump2version major --allow-dirty
	git push
	git push --tags
