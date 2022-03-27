import numpy as np
import matplotlib.pyplot as plt
from abg_interpreter import interpret_as_str
from abg_data import REGION_DICT

L = ["I don't know"] + list(REGION_DICT.keys())
print(L)

test_space = np.linspace([7.0, 0], [7.8, 56], num=500)
answer_space = []
for lab in test_space:
    ph, bicarb = lab
    s = interpret_as_str(ph, bicarb)
    i = L.index(s)
    answer_space.append(i)



A = np.array(answer_space)
# print(A)

over = test_space[:,0] > 7.35
under = test_space[:,0] < 7.45
v = np.vstack((over, under))
conjunction = np.all(v, axis=0)
found = test_space[np.nonzero(conjunction), :]
print(found)
