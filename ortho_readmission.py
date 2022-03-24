import numpy as np
import pandas as pd


class Model:
    def __init__(self, bias: float, age_y: float, bmi: float, bmisq,
                 gender: float, dysrhythmia: float, heart_failure: float, dys_hf_interaction: float,
                 discharge_home_self: float, discharge_facility: float, ed_visits: float, psych_dx: float,
                 pta_med_count: float, drug_abuse_dx: float, narcotic_meds: float, tja_within_past_yr: float):
        """Input regression coefficients as positional or named parameters.
        Keep them organized and expose list or data frame. Note: 16 coefficients.
        """
        self.as_list = [bias, age_y, bmi, bmisq,
                        gender, dysrhythmia, heart_failure, dys_hf_interaction,
                        discharge_home_self, discharge_facility, ed_visits, psych_dx,
                        pta_med_count, drug_abuse_dx, narcotic_meds, tja_within_past_yr]
        row_names = ['bias', 'age_y', 'bmi', 'bmi ** 2',
                     '(gender == male)', 'dysrhythmia', 'heart_failure', 'dysrhythmia * heart_failure',
                     'disch_home_or_self', 'disch_facility', '(ed_visits > 9)', 'psych_dx',
                     'pta_med_count', 'drug_abuse_dx', 'narcotic_meds', 'TJA within past yr']
        self.as_dataframe = pd.DataFrame(self.as_list, index=row_names)


class Patient:
    def __init__(self, age_y: float, bmi: float, gender: str, dysrhythmia: bool,
                 heart_failure: bool, discharge: str, ed_visits: int, psych_dx: bool,
                 pta_med_count: float, drug_abuse_dx: bool, narcotic_meds: bool, tja_within_past_12_mo: bool):
        """Input 12 patient characteristics as positional or named parameters.
        Keep them organized.
        Expose list of 16 numbers, for multiplying with model coefficients.
        """
        # self.age_y = age_y
        # self.bmi = bmi
        # self.gender = gender
        # self.dysrhythmia = dysrhythmia
        # self.heart_failure = heart_failure
        # self.discharge = discharge
        # self.ed_visits = ed_visits
        # self.psych_dx = psych_dx
        # self.pta_med_count = pta_med_count
        # self.drug_abuse_dx = drug_abuse_dx
        # self.narcotic_meds = narcotic_meds
        # self.tja_within_past_12_mo = tja_within_past_12_mo
        self.as_list = [1, age_y,
                        bmi, bmi ** 2,
                        gender == 'male', dysrhythmia,
                        heart_failure, dysrhythmia and heart_failure,
                        discharge == 'home' or discharge == 'self-care', discharge == 'facility',
                        ed_visits > 9, psych_dx,
                        pta_med_count, drug_abuse_dx,
                        narcotic_meds, tja_within_past_12_mo]


model_90_days = Model(
    -0.5527,
    0,  # age
    -0.0903,  # bmi
    0.00145,  # bmi ** 2
    0.2241,  # (gender == 'male')
    -0.1169,  # dysrhythmia
    -0.1284,  # heart_failure
    0.7544,  # dysrhythmia * heart_failure
    -0.2464,  # (discharge == 'home' or discharge == 'self-care')
    0.3233,  # (discharge == 'facility')
    0.3325,  # (ed_visits > 9)
    0,  # psych dx
    0.0193,  # pta_med_count
    0.2475,  # drug_abuse_dx
    0.1296,  # narcotic_meds
    -0.3820  # tja_within_past_12_mo
)

model_30_days = Model(-2.6576, 0.0291, -0.1345, 0.00218,
                      0.2070, -0.0505, -0.3669, 0.7994,
                      -0.3124, 0.3645, 0.5942, 0.1934,
                      0.0332, 0, 0, 0)

p = Patient(65, 30, 'male', True,
            True, 'home', 3, False,
            5, False, True, False)

if __name__ == '__main__':
    print("Patient, length =", len(p.as_list))
    print(p.as_list)
    print()

    print("Model, length =", len(model_30_days.as_list))
    print(model_30_days.as_list)
    print()

    print("Score =", np.dot(p.as_list, model_30_days.as_list))
