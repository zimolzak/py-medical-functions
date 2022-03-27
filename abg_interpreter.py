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
    answers = {}
    for k, region in d.items():
        answers[k] = region.contains([ph, bicarb])
    return answers


def interpret_as_str(ph: float, bicarb: float) -> str:
    answers = interpret(ph, bicarb)
    if sum(answers.values()) > 1:
        raise ValueError("Lab maps to more than 1 disorder??")
    for k, v in answers.items():
        if v:
            return k
    return "I don't know"
