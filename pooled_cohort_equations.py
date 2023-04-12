"""
Goff DC Jr, Lloyd-Jones DM, Bennett G, et al.

2013 ACC/AHA guideline on the assessment of cardiovascular risk: a
report of the American College of Cardiology/American Heart Association Task Force on Practice Guidelines

[published
correction appears in Circulation. 2014 Jun 24;129(25 Suppl 2):S74-5].

Circulation. 2014;129(25 Suppl 2):S49-S73.

doi:10.1161/01.cir.0000437741.48606.98

https://pubmed.ncbi.nlm.nih.gov/24222018/

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
    -3.114,  #
    -13.578,
    3.149,
    2.019,
    'N/A',
    1.957,
    'N/A',
    7.574,
    -1.665,
    0.661
]
