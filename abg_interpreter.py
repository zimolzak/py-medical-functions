from abg_data import met_acidosis_reg, met_alkalosis_reg,\
    acute_resp_acidosis_reg, acute_resp_alkalosis_reg,\
    chronic_resp_alkalosis_reg, chronic_resp_acidosis_reg




REGION_DICT = {'mac': met_acidosis_reg, 'arac': acute_resp_acidosis_reg, 'crac': chronic_resp_acidosis_reg,
               'malk': met_alkalosis_reg, 'aralk': acute_resp_alkalosis_reg, 'cralk': chronic_resp_alkalosis_reg}


def interpret(ph, bicarb, d=None):
    if d is None:
        d = REGION_DICT
    answers = {}
    for k, region in d.items():
        answers[k] = region.contains([ph, bicarb])
    return answers


if __name__ == '__main__':
    print("norm ", interpret(7.4, 24))  # normal fixme - "ignore" should test x < > vertical line?
    print("mac  ", interpret(7.2, 8))  # mac  fixme - has malk also
    print("arac ", interpret(7.125, 27))  # arac -  fixme aralk
    print("malk ", interpret(7.55, 40))  # malk fixme does not detect
    print("aralk", interpret(7.6, 20))  # aralk fixme 3 answers
