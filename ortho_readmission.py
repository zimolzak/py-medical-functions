def score(age_y: float, BMI: float, gender: str, CD: bool, HF: bool, discharge: str,
          ED_visits: int, psych_Dx: bool, PTA_med_count: float) -> float:
    """Source: Greiwe RM, Spanyer JM, Nolan JR, Rodgers RN, Hill MA, Harm RG. Improving Orthopedic Patient Outcomes:
    A Model to Predict 30-Day and 90-Day Readmission Rates Following Total Joint Arthroplasty. J Arthroplasty. 2019
    Nov;34(11):2544-2548. doi: 10.1016/j.arth.2019.05.051. Epub 2019 Jun 5. PMID: 31272826.

    :param age_y:
    :param BMI:
    :param gender:
    :param CD:
    :param HF:
    :param discharge:
    :param ED_visits:
    :param psych_Dx:
    :param PTA_med_count:
    :return:
    """
    Y = -2.6576 + 0.0291 * age_y - 0.1345 * BMI + 0.00218 * BMI ** 2 + \
        0.2070 * (gender == 'male') - 0.0505 * (CD == True) - 0.3669 * (HF == True) + \
        0.7994 * (CD == True) * (HF == True) - \
        0.3124 * (discharge == 'home' or discharge == 'self-care') + \
        0.3645 * (discharge == 'facility') + 0.5942 * (ED_visits > 9) + \
        0.1934 * (psych_Dx == True) + 0.0332 * PTA_med_count

    return Y
