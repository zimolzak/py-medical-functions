from abg_data import met_acidosis_reg, met_alkalosis_reg,\
    acute_resp_acidosis_reg, acute_resp_alkalosis_reg,\
    chronic_resp_alkalosis_reg, chronic_resp_acidosis_reg
from abg_interpreter import interpret, interpret_as_str


ABG = {'mac': [7.2, 8], 'arac': [7.125, 27], 'extreme': [7.11, 28],
       'crac': [7.35, 36], 'malk': [7.55, 40],
       'aralk': [7.6, 20], 'cralk': [7.45, 16],
       'normal': [7.4, 24]
       }


def test_region_contains():
    assert met_acidosis_reg.contains(ABG['mac'])
    assert acute_resp_acidosis_reg.contains(ABG['arac'])
    assert not acute_resp_acidosis_reg.contains(ABG['extreme'])
    assert chronic_resp_acidosis_reg.contains(ABG['crac'])
    assert met_alkalosis_reg.contains(ABG['malk'])
    assert acute_resp_alkalosis_reg.contains(ABG['aralk'])
    assert chronic_resp_alkalosis_reg.contains(ABG['cralk'])


def n_true(region_str: str):
    interp_dict = interpret(ABG[region_str][0],
                            ABG[region_str][1])
    return sum(interp_dict.values())


def test_interpret_crac():
    assert n_true('crac') == 1


def test_interpret_extreme():
    assert n_true('extreme') == 0


def test_interpret_cralk():
    assert n_true('cralk') == 1


def test_interpret_mac():
    assert n_true('mac') == 1


def test_interpret_malk():
    assert n_true('malk') == 1


def test_interpret_normal():
    assert n_true('normal') == 1


def test_interpret_arac():
    assert n_true('arac') == 1


def test_interpret_aralk():
    assert n_true('aralk') == 1


def test_interpret_as_str():
    ph, bicarb = ABG['mac']
    assert interpret_as_str(ph, bicarb) == 'mac'
