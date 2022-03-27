from abg_data import met_acidosis_reg, met_alkalosis_reg, \
    acute_resp_acidosis_reg, acute_resp_alkalosis_reg, \
    chronic_resp_alkalosis_reg, chronic_resp_acidosis_reg
from abg_interpreter import interpret, interpret_as_str

TEST_POINTS = {'mac': [7.2, 8], 'arac': [7.125, 27], 'extreme': [7.11, 28],
               'crac': [7.35, 36], 'malk': [7.55, 40],
               'aralk': [7.6, 20], 'cralk': [7.45, 16],
               'normal': [7.4, 24]
               }


def test_region_contains():
    assert met_acidosis_reg.contains(TEST_POINTS['mac'])
    assert acute_resp_acidosis_reg.contains(TEST_POINTS['arac'])
    assert not acute_resp_acidosis_reg.contains(TEST_POINTS['extreme'])
    assert chronic_resp_acidosis_reg.contains(TEST_POINTS['crac'])
    assert met_alkalosis_reg.contains(TEST_POINTS['malk'])
    assert acute_resp_alkalosis_reg.contains(TEST_POINTS['aralk'])
    assert chronic_resp_alkalosis_reg.contains(TEST_POINTS['cralk'])


def n_true(region_str: str) -> int:
    interp_dict = interpret(TEST_POINTS[region_str][0],
                            TEST_POINTS[region_str][1])
    return sum(interp_dict.values())


def both_tests(s: str) -> None:
    ph, bicarb = TEST_POINTS[s]
    assert n_true(s) == 1
    assert interpret_as_str(ph, bicarb) == s


def test_interpret_crac():
    both_tests('crac')


def test_interpret_extreme():
    e = 'extreme'
    ph, bicarb = TEST_POINTS[e]
    assert n_true(e) == 0
    assert interpret_as_str(ph, bicarb) == "I don't know"


def test_interpret_cralk():
    both_tests('cralk')


def test_interpret_mac():
    both_tests('mac')


def test_interpret_malk():
    both_tests('malk')


def test_interpret_normal():
    both_tests('normal')


def test_interpret_arac():
    both_tests('arac')


def test_interpret_aralk():
    both_tests('aralk')
