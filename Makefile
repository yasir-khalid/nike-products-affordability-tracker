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
	@conda env export > environment.yml

setup: health
	@pip install -r requirements.txt
	@$(support-libs)
	@npx dotenv-vault login

run: setup
	@python main.py

format:
	@isort *.py
	@black *.py

push-env:
	@npx dotenv-vault push

pull-env:
	@npx dotenv-vault pull

vault-login:
	@npx dotenv-vault login
# test:
# 	python -m pytest -vv test_main.py




