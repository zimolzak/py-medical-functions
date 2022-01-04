from meld import meld


def test_meld():
    # straight from OPTN meld calculator
    # https://optn.transplant.hrsa.gov/data/allocation-calculators/meld-calculator/

    #            na  inr  tb   cr
    assert meld(140, 1.0, 1.0, 1.0) == 6
    assert meld(140, 1.2, 1.2, 1.2) == 11
    assert meld(140, 1.2, 1.3, 1.4) == 13
    assert meld(140, 2, 3, 4) == 32
    assert meld(140, 3, 20, 4) == 40
    # assert meld(120, 4, 4, 2.5) == 38  # round at end
