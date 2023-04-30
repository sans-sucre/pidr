VENV = venv
PYTHON = $(VENV)/bin/python3
PIP = $(VENV)/bin/pip

run : $(VENV)/bin/activate
	$(PYTHON) azi_scrapper.py
	$(PYTHON)
