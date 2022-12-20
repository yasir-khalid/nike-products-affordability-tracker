define support-libs
	@pip install black
	@pip install isort
endef

health:
	@make --version
	@python --version

freeze:
	@pip install pipreqs
	@pipreqs . --force

setup: health
	@pip install --upgrade pip
	@pip install -r requirements.txt
	@$(support-libs)

run: setup
	@python main.py

format:
	@isort *.py
	@black *.py
	
# test:
# 	python -m pytest -vv test_main.py




