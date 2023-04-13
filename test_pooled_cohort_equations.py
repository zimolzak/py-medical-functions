import numpy as np
import itertools
from pooled_cohort_equations import pce
from test_meld import float_range

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


def test_many():
    age = float_range(40, 70, 5)
    sex = ['F', 'M']
    race = ['W', 'AA']
    tc = float_range(190, 250, 10)
    hdl = float_range(30, 70, 10)
    sbp = float_range(110, 150, 10)
    tf = [True, False]
    p = itertools.product(age, sex, race, tc, hdl, sbp, tf, tf, tf)
    n = 0
    for my_tuple in p:
        assert pce(*my_tuple) < 1
        assert pce(*my_tuple) > 0
        n += 1
    print('\n', n, "throwaways done")
