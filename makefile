dependencies = test_meld.py meld.py
dependencies += test_pooled_cohort_equations.py pooled_cohort_equations.py
dependencies += abg_interpreter.py test_abg_interpreter.py abg_data.py abg_functions.py

htmlcov/index.html: $(dependencies)
	py.test --cov=. --cov-report html
