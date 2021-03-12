PY = python3
PYTEST = pytest
PYTESTFLAGS = --cov

SRC = Questions
COV = --cov-report term-missing

RMDIR = rm -rf

test:
	$(PYTEST) $(PYTESTFLAGS) $(SRC) $(COV)

clean:	
	@- $(RMDIR) .pytest_cache
	@- $(RMDIR) .coverage
	cd Questions
	@- $(RMDIR) **/*__pycache__