htmlcov/index.html: test_meld.py meld.py
	py.test --cov=. --cov-report html
