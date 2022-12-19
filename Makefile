# Variables
REQUIREMENTS:="requirements.txt"

VENV_BIN_DIR:="venv/bin"
CMD_FROM_VENV:=". $(VENV_BIN_DIR)/activate; which"
VIRTUALENV:=$(shell which virtualenv)
PIP:="$(VENV_BIN_DIR)/pip"

PYTHON=$(shell "$(CMD_FROM_VENV)" "python")
# supporting functions
define create-venv
virtualenv venv -p python3
endef

# MAKE commands
hello:
	@echo "Hello world from Makefile"

venv:
	@$(create-venv)
	@$(PIP) install -r $(REQUIREMENTS_LOCAL)

freeze:
	@$(CMD_FROM_VENV)
	@pip install pipreqs
	@pipreqs . --force

setup:
	@pip install --upgrade pip &&\
		pip install -r requirements.txt

run: setup
	@python main.py

health-check:
	@echo "Checking if all the required environment variables are assigned"

format:
	@black *.py

# test:
# 	python -m pytest -vv test_main.py




