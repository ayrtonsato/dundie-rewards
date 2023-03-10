.PHONY: install virtualenv ipython clean test watch lint fmt build publish-test publish

install:
	@echo "Installing for dev environment"
	@.venv/bin/python -m pip install -e '.[test,dev]'

virtualenv:
	@python3 -m venv .venv

ipython:
	@.venv/bin/ipython

test:
	@.venv/bin/pytest -s --forked

watch:
	#@@.venv/bin/ptw
	@ls **/*.py | entr pytest --forked

lint:
	@.venv/bin/pflake8

fmt:
	@.venv/bin/isort --profile=black -m 3 dundie tests integration
	@.venv/bin/black dundie tests integration

clean:            ## Clean unused files.
	@find ./ -name '*.pyc' -exec rm -f {} \;
	@find ./ -name '__pycache__' -exec rm -rf {} \;
	@find ./ -name 'Thumbs.db' -exec rm -f {} \;
	@find ./ -name '*~' -exec rm -f {} \;
	@rm -rf .cache
	@rm -rf .pytest_cache
	@rm -rf .mypy_cache
	@rm -rf build
	@rm -rf dist
	@rm -rf *.egg-info
	@rm -rf htmlcov
	@rm -rf .tox/
	@rm -rf docs/_build

build:
	@python setup.py sdist bdist_wheel

publish-test:
	@twine upload --repository testpypi dist/* --verbose

publish:
	@twine upload dist/*
