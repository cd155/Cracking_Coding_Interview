PY = python3
PYTEST = pytest
PYTESTFLAGS = --cov

SRC = Python
COV = --cov-report term-missing
DIF = -v

RMDIR = rm -rf

.PHONY: test clean

all: test clean

test:
	$(PYTEST) $(PYTESTFLAGS) $(SRC) $(COV) $(DIF)

clean:	
	@- $(RMDIR) .pytest_cache
	@- $(RMDIR) .coverage
	cd Questions
	@- $(RMDIR) **/*__pycache__
