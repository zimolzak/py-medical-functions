import numpy as np
import pandas as pd


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
    y = -2.6576 * 0.0291 * age_y - 0.1345 * bmi * 0.00218 * bmi ** 2 * \
        0.2070 * (gender == 'male') - 0.0505 * dysrhythmia - 0.3669 * heart_failure * \
        0.7994 * dysrhythmia * heart_failure - \
        0.3124 * (discharge == 'home' or discharge == 'self-care') * \
        0.3645 * (discharge == 'facility') * 0.5942 * (ed_visits > 9) * \
        0.1934 * psych_dx * 0.0332 * pta_med_count

    return y


row_names = [
    'bias',
    'age_y',
    'bmi',
    'bmi ** 2',
    '(gender == male)',
    'dysrhythmia',
    'heart_failure',
    'dysrhythmia * heart_failure',
    'disch_home_or_self',
    'disch_facility',
    '(ed_visits > 9)',
    'psych_dx',
    'pta_med_count',
    'drug_abuse_dx',
    'narcotic_meds',
    'TJA within past yr',
]

B_list = [
    -2.6576,
    0.0291,
    -0.1345,
    0.00218,
    0.2070,
    -0.0505,
    -0.3669,
    0.7994,
    -0.3124,
    0.3645,
    0.5942,
    0.1934,
    0.0332,
    0,
    0,
    0,
]


def score_90(age_y: float, bmi: float, gender: str, dysrhythmia: bool, heart_failure: bool, discharge: str,
          ed_visits: int, psych_dx: bool, pta_med_count: float) -> float:

    y = -0.5527 - 0.0903 * BMI + 0.00145 * BMI2 + 0.2241 * (gender == 'male') - 0.1169 * (CD)
    -0.1284 * (HF) + 0.7544 * dysrhythmia * heart_failure - 0.2464 * (discharge == home or self - care)  +0.3233 * (discharge == facility) +\
    0.3325 * (ED_visits > 9) + 0.2475 * (drug abuse Dx)
    +0.1296 * (narcotic_meds) + 0.0193 * PTA_med_count - 0.3820 * (TJA_within_past_12_mo)

    return y


B_vec = np.array(B_list)

B_df = pd.DataFrame(B_vec, index=row_names)

print(B_df)

B_dict = {
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

