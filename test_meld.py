from meld import meld
import itertools


def float_range(low, hi, step):
    value = low
    yield value
    while value <= (hi - step):
        value += step
        yield value


def test_meld():
    # straight from OPTN meld calculator
    # https://optn.transplant.hrsa.gov/data/allocation-calculators/meld-calculator/

    #            na  inr  tb   cr
    assert meld(140, 1.0, 1.0, 1.0) == 6
    assert meld(140, 1.2, 1.2, 1.2) == 11
    assert meld(140, 1.2, 1.3, 1.4) == 13
    assert meld(140, 2, 3, 4) == 32
    assert meld(140, 3, 20, 4) == 40
    assert meld(120, 4, 4, 2.5) == 38  # round at end


def test_without_expectation():
    na_range = float_range(120, 150, 2)  # 31 if step = 1
    inr_range = float_range(0.8, 4.0, 0.2)   # 41 if step = 0.1
    tb_range = float_range(0.8, 20, 0.4)   # 193  if step = 0.1
    cr_range = float_range(0.8, 5.0, 0.2)  # 43 if step = 0.1
    # fixme - maybe should do @pytest.mark.parametrize but I don't know how to use it yet.
    # 8189952 elements in the product if steps as above takes 13 sec = 630k / sec
    # steps increased --> 263424 throwaways
    p = itertools.product(na_range, inr_range, tb_range, cr_range)
    n = 0
    for my_tuple in p:
        throw_away = meld(*my_tuple)
        n += 1
    print(n, "throwaways done")


if __name__ == '__main__':
    test_without_expectation()  # "python test_meld.py" to see printout count.
