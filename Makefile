debug:
	make --version

generate-requirements:
	pip install pipreqs &&\
		pipreqs . --force

setup:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

run:
	python main.py

health-check:
	echo "Checking if all the required environment variables are assigned"

format:
	black *.py
	
# test:
# 	python -m pytest -vv test_main.py




