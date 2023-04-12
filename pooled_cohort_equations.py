"""
Goff DC Jr, Lloyd-Jones DM, Bennett G, et al.
2013 ACC/AHA guideline on the assessment of cardiovascular risk:
a report of the American College of Cardiology/American Heart Association Task Force on Practice Guidelines
[published correction appears in Circulation. 2014 Jun 24;129(25 Suppl 2):S74-5].
Circulation. 2014;129(25 Suppl 2):S49-S73.
doi:10.1161/01.cir.0000437741.48606.98
https://pubmed.ncbi.nlm.nih.gov/24222018/

Mainly Table A in paper, or Table 4 in full work group report Word doc.
"""

import numpy as np

"""
Ln Age (y)
Ln Age, Squared
Ln Total Cholesterol (mg/dL)
Ln Age×Ln Total Cholesterol
Ln HDL-C (mg/dL)
Ln Age×Ln HDL-C 
Log Treated Systolic BP (mm Hg)
Log Age×Log Treated Systolic BP
Log Untreated Systolic BP (mm Hg)
Log Age×Log Untreated Systolic BP
Current Smoker (1=Yes, 0=No)
Log Age×Current Smoker
Diabetes (1=Yes, 0=No
"""

white_women = [
    -29.799,  # age
    4.884,  # age sq
    13.540,  # tc
    -3.114,  # age tc
    -13.578,  # hdl
    3.149,  # age hdl
    2.019,  # tbp
    0,  # age tbp
    1.957,  # ubp
    0,  # age ubp
    7.574,  # smok
    -1.665,  # age smok
    0.661  # diab
]

af_am_women = [
    17.114,
    0,
    0.940,
    0,
    -18.920,
    4.475,
    29.291,
    -6.432,
    27.820,
    -6.087,
    0.691,
    0,
    0.874
]

white_men = [
    12.344,  # age
    11.853,  # tc
    -2.664,  # age tc
    -7.990,  # hdl
    1.769,  # age hdl
    1.797,  # tbp
    1.764,  # ubp
    7.837,  # smok
    -1.795,  # age smok
    0.658  # diab
]

af_am_men = [
    2.469,
    0.302,
    0,
    -0.307,
    0,
    1.916,
    1.809,
    0.549,
    0,
    0.645
]


def pce(age: float, sex: str, race: str, tc: float, hdl: float, sbp: float, treated: bool, smoker: bool,
        diabetes: bool) -> float:
    """Calculate 10-year risk for hard ASCVD

    :param race:
    :param sex:
    :param age: Age in years
    :param tc: Total cholesterol, mg/dL
    :param hdl: HDL cholesterol, mg/dL
    :param sbp: systolic blood pressure, mmHg
    :param treated: is blood pressure treated?
    :param smoker: current smoker?
    :param diabetes: has diabetes?
    :return:
    """

    if treated:
        log_tbp = np.log(sbp)
        log_ubp = 0
    else:
        log_tbp = 0
        log_ubp = np.log(sbp)

    if sex == 'F':
        if race == 'W':
            coefficients = white_women
        elif race == 'AA':
            coefficients = af_am_women
        else:
            raise ValueError('race {} should be "W" or "AA"'.format(race))

        values = [
            np.log(age),
            np.log(age) ** 2,
            np.log(tc),
            np.log(age) * np.log(tc),
            np.log(hdl),
            np.log(age) * np.log(hdl),
            log_tbp,
            np.log(age) * log_tbp,
            log_ubp,
            np.log(age) * log_ubp,
            smoker,
            np.log(age) * smoker,
            diabetes
        ]
    elif sex == 'M':
        raise NotImplementedError  # fixme
    else:
        raise ValueError('sex {} should be "M" or "F"'.format(sex))

    individual_sum = np.dot(values, coefficients)
    means = {'WF': -29.18, 'AAF': 86.61, 'WM': 61.18, 'AAM': 18.97}
    baselines = {'WF': 0.9665, 'AAF': 0.9533, 'WM': 0.9144, 'AAM': 0.8954}
    specific_mean = means[race + sex]
    specific_baseline = baselines[race + sex]

    return 1 - specific_baseline ** (np.exp(individual_sum - specific_mean))


print(pce(55, 'F', 'AA', 200, 50, 120, False, False, False))
print(pce(55, 'F', 'W', 200, 50, 120, False, False, False))
