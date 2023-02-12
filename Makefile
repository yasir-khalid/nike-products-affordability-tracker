define support-libs
	@pip install black
	@pip install isort
endef

define vault-login:
	@npx dotenv-vault login -y
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
	@$(vault-login)

run: setup
	@python main.py

format:
	@isort *.py
	@black *.py

push-env:
	@npx dotenv-vault push

pull-env:
	@npx dotenv-vault pull

dotenv-vault: 
	@npx dotenv-vault open -y
	# alternatively you can visit `ui.dotenv.org`

# test:
# 	python -m pytest -vv test_main.py




