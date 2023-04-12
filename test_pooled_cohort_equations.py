import numpy as np
from pooled_cohort_equations import pce

example_percents = np.array([2.1, 3.0, 5.3, 6.1])  # taken straight from example table in Circulation paper


def test_pce():
    my_proportions = np.array([
        pce(55, 'F', 'W', 213, 50, 120, False, False, False),
        pce(55, 'F', 'AA', 213, 50, 120, False, False, False),
        pce(55, 'M', 'W', 213, 50, 120, False, False, False),
        pce(55, 'M', 'AA', 213, 50, 120, False, False, False)
    ])

    my_percents = my_proportions * 100
    assert np.max(example_percents - my_percents) < 0.1
