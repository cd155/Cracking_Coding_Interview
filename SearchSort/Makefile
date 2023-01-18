PYTEST = pytest
PYTESTFLAGS = --cov

COV = --cov-report term-missing
DIF = -v

RMDIR = rm -rf

.PHONY: test clean

all: test clean

test:
	$(PYTEST) $(PYTESTFLAGS) $(COV) $(DIF)

clean:	
	@- $(RMDIR) .pytest_cache
	@- $(RMDIR) .coverage
	@- $(RMDIR) __pycache__
