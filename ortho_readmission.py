def score(age_y, BMI, gender, CD,  HF, discharge, ED_visits, psych_Dx, PTA_med_count):

    Y = -2.6576 + 0.0291 * age_y - 0.1345 * BMI + 0.00218 * BMI**2 + \
        0.2070 * (gender == 'male') - 0.0505 * (CD == True) - 0.3669 * (HF == True) + \
        0.7994 * ( CD == True) * (HF == True) - \
        0.3124 * (discharge == 'home' or discharge  == 'self-care') + \
        0.3645 * (discharge == 'facility') + 0.5942 * (ED_visits > 9) + \
        0.1934 * (psych_Dx == True) + 0.0332 * PTA_med_count

    return Y
