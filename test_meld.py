from meld import meld


def test_meld():
    # straight from optn meld calculator
    # https://optn.transplant.hrsa.gov/data/allocation-calculators/meld-calculator/
    assert meld(140, 1.0, 1.0, 1.0) == 6
    assert meld(120, 4, 4, 2.5) == 38
