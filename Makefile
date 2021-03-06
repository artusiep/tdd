init-project:
	python -m venv venv
	( \
		. venv/bin/activate; \
		pip3 install -r requirements.txt; \
	)

run-trivial:
	python cli.py -t

run-complex:
	python cli.py -c

run-summary:
	python cli.py -s

run-interiactive-cli:
	python cli_interactive.py