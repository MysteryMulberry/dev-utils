PYTHON ?= python
VENV = .venv

.PHONY: venv install test lint clean

venv:
	$(PYTHON) -m venv $(VENV)

install: venv
	$(VENV)/bin/pip install -r requirements.txt

test:
	$(VENV)/bin/pytest -v

lint:
	$(VENV)/bin/ruff check .
	$(VENV)/bin/mypy .

clean:
	rm -rf $(VENV) __pycache__ .pytest_cache dist build *.egg-info
