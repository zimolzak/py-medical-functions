from abg_data import REGION_DICT


def interpret(ph: float, bicarb: float, d: dict = None) -> dict:
    """Interpret an arterial blood gas (ABG).

    :param ph: Measured pH of the ABG
    :param bicarb: Bicarbonate level of the ABG
    :param d: dict of abnormality names and Region objects (need not be Region, just obj with .contains() method)
    :return: Dict of names and True/False values (whether the pH and bicarb fall within each region)
    """
    if d is None:
        d = REGION_DICT
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


def interpret_as_str(ph: float, bicarb: float, d: dict = None) -> str:
    return "I don't know"
