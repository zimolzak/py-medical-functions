from abg_data import met_acidosis_reg, met_alkalosis_reg, \
    acute_resp_acidosis_reg, acute_resp_alkalosis_reg, \
    chronic_resp_alkalosis_reg, chronic_resp_acidosis_reg


def interpret(ph: float, bicarb: float, d: dict = None) -> dict:
    """Interpret an arterial blood gas (ABG).

    :param ph: Measured pH of the ABG
    :param bicarb: Bicarbonate level of the ABG
    :param d: dict of abnormality names and Region objects (need not be Region, just obj with .contains() method)
    :return: Dict of names and True/False values (whether the pH and bicarb fall within each region)
    """
    if d is None:
        d = {'mac': met_acidosis_reg, 'arac': acute_resp_acidosis_reg,
             'crac': chronic_resp_acidosis_reg, 'malk': met_alkalosis_reg,
             'aralk': acute_resp_alkalosis_reg, 'cralk': chronic_resp_alkalosis_reg}
    if 7.35 <= ph <= 7.45 and 22 <= bicarb <= 24:
        # normal
        k = d.keys()
        answers = dict(zip(k, [False] * len(k)))
        answers['normal'] = True
        return answers
    else:
        answers = {}
        for k, region in d.items():
            answers[k] = region.contains([ph, bicarb])
        answers['normal'] = False
        return answers
