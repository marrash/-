.PHONY: gen_requirements install_requirements run

gen_requirements:
	rm -f requirements.txt
	pipreqs ./

install_requirements:
	pip install -r requirements.txt

run:
	python3 ./slot_testflow.py