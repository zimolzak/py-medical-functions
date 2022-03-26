from abg_interpreter import met_acidosis_reg, met_alkalosis_reg,\
    acute_resp_acidosis_reg, acute_resp_alkalosis_reg,\
    chronic_resp_alkalosis_reg, chronic_resp_acidosis_reg,\
    interpret


ABG = {'mac': [7.2, 8], 'arac': [7.125, 27], 'extreme': [7.11, 28],
       'crac': [7.35, 36], 'malk': [7.55, 40], 'aralk': [7.6, 20], 'cralk': [7.45, 16]}


def test_region():
    assert met_acidosis_reg.contains(ABG['mac'])
    assert acute_resp_acidosis_reg.contains(ABG['arac'])
    assert not acute_resp_acidosis_reg.contains(ABG['extreme'])
    assert chronic_resp_acidosis_reg.contains(ABG['crac'])
    assert met_alkalosis_reg.contains(ABG['malk'])
    assert acute_resp_alkalosis_reg.contains(ABG['aralk'])
    assert chronic_resp_alkalosis_reg.contains(ABG['cralk'])


def test_interpret():
    interpret(ABG['crac'][0], ABG['crac'][1])
    # fixme count up how many True
