# to run this file on CLI --> make install , make virtualenv_installation, make test

install:
	@echo "Installing the program"

virtualenv_installation:
	@echo "Installing Virtual Env"
	python -m venv .venv

install_requirements:
	@echo 'Installing Requirements'
	pip install -r requirements.txt -r requirements.test.txt -r requirements.dev.txt

upgrade_pip:
	@echo 'Upgrading Pip'
	@.venv/bin/python -m pip install --upgrade pip

test:
	@.venv/bin/pytest -vv -s tests/
