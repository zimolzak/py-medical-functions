import numpy as np
import matplotlib.pyplot as plt
from abg_interpreter import interpret_as_str
from abg_data import REGION_DICT

L = ["I don't know"] + list(REGION_DICT.keys())
print("Possible interpreter answers are:")
print(L)

x, y = np.mgrid[7.0:7.8:0.02, 0:56:1]
test_space = np.vstack((x.ravel(), y.ravel()))
test_space = test_space.transpose()
print("Matrix of points to test has shape {}".format(test_space.shape))
print()

answer_space = np.zeros(test_space.shape[0])
for i, lab in enumerate(test_space):
    ph, bicarb = lab
    try:
        s = interpret_as_str(ph, bicarb)
    except ValueError as e:
        print("Exception at", ph, bicarb, ":", e)
    x = L.index(s)  # fixme - might have to define 's' when exception?
    answer_space[i] = x

A = np.array(answer_space)

colors = ['black', 'red', 'orange', 'yellow', 'green', 'blue', 'purple', 'grey']

for i in range(len(L)):
    indices = np.nonzero(A == i)
    yi = test_space[indices, 1]
    xi = test_space[indices, 0]
    plt.plot(xi, yi, marker='o', color=colors[i])

plt.savefig('outoutout.png')

# over = test_space[:, 0] > 7.35
# under = test_space[:, 0] < 7.45
# v = np.vstack((over, under))
# conjunction = np.all(v, axis=0)
# found = test_space[np.nonzero(conjunction), :]
# print(found)
