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
    'N/A',  # age tbp
    1.957,  # ubp
    'N/A',  # age ubp
    7.574,  # smok
    -1.665,  # age smok
    0.661  # diab
]

af_am_women = [
    17.114,
    'N/A',
    0.940,
    'N/A',
    -18.920,
    4.475,
    29.291,
    -6.432,
    27.820,
    -6.087,
    0.691,
    'N/A',
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
    'N/A',
    -0.307,
    'N/A',
    1.916,
    1.809,
    0.549,
    'N/A',
    0.645
]
