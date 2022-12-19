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

# test:
# 	python -m pytest -vv test_main.py

# format:
# 	black *.py


