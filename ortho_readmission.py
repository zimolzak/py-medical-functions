def score(age_y: float, bmi: float, gender: str, dysrhythmia: bool, heart_failure: bool, discharge: str,
          ed_visits: int, psych_dx: bool, pta_med_count: float) -> float:
    """Source: Greiwe RM, Spanyer JM, Nolan JR, Rodgers RN, Hill MA, Harm RG. Improving Orthopedic Patient Outcomes:
    A Model to Predict 30-Day and 90-Day Readmission Rates Following Total Joint Arthroplasty. J Arthroplasty. 2019
    Nov;34(11):2544-2548. doi: 10.1016/j.arth.2019.05.051. Epub 2019 Jun 5. PMID: 31272826.

    :param age_y:
    :param bmi:
    :param gender:
    :param dysrhythmia:
    :param heart_failure:
    :param discharge:
    :param ed_visits:
    :param psych_dx:
    :param pta_med_count:
    :return:
    """
    y = -2.6576 + 0.0291 * age_y - 0.1345 * bmi + 0.00218 * bmi ** 2 + \
        0.2070 * (gender == 'male') - 0.0505 * dysrhythmia - 0.3669 * heart_failure + \
        0.7994 * dysrhythmia * heart_failure - \
        0.3124 * (discharge == 'home' or discharge == 'self-care') + \
        0.3645 * (discharge == 'facility') + 0.5942 * (ed_visits > 9) + \
        0.1934 * psych_dx + 0.0332 * pta_med_count

    return y


beta_30 = {
    'bias': -2.6576,
    'age_y': 0.0291,
    'bmi': -0.1345,
    'bmi ** 2': 0.00218,
    '(gender == male)': 0.2070,
    'dysrhythmia': -0.0505,
    'heart_failure': -0.3669,
    'dysrhythmia * heart_failure': 0.7994,
    'disch_home_or_self': -0.3124,
    'disch_facility': 0.3645,
    '(ed_visits > 9)': 0.5942,
    'psych_dx': 0.1934,
    'pta_med_count': 0.0332,
}
