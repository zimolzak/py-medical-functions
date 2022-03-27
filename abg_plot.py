import numpy as np
import matplotlib.pyplot as plt
from abg_interpreter import interpret_as_str
from abg_data import REGION_DICT

L = ["I don't know"] + list(REGION_DICT.keys())
print(L)

x, y = np.mgrid[7.0:7.8:0.02, 0:56:1]
test_space = np.vstack((x.ravel(), y.ravel()))
test_space = test_space.transpose()

answer_space = []
for lab in test_space:
    ph, bicarb = lab
    try:
        s = interpret_as_str(ph, bicarb)
    except ValueError as e:
        print(ph, bicarb, e)
    i = L.index(s)
    answer_space.append(i)

A = np.array(answer_space)

for i in range(len(L)):
    indices = np.nonzero(A == i)
    yi = test_space[indices, 1]
    xi = test_space[indices, 0]
    plt.plot(xi, yi, 'o')
    # print(i)
    # print(np.argwhere(A == i))
    # print()
    # print()

plt.savefig('outoutout.png')


#  print(A)

# over = test_space[:, 0] > 7.35
# under = test_space[:, 0] < 7.45
# v = np.vstack((over, under))
# conjunction = np.all(v, axis=0)
# found = test_space[np.nonzero(conjunction), :]
# print(found)
