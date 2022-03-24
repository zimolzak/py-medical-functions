import numpy as np


class Parabola:
    def __init__(self, x1, y1, x2, y2, x3, y3):
        """Define a parabolic curve from 3 points.

        Given points are x1,y1 .. x3,y3.
        Want to find coeffs a, b, c for general eqn y = a x^2 + b x + c .
        Do this by solving system (matrix eqn) M * x = n , which is a system of
        (a * x1^2) + (b * x1) + (c * 1) = y1
        """

        m = np.array([[x1 ** 2, x1, 1],
                      [x2 ** 2, x2, 1],
                      [x3 ** 2, x3, 1]])
        n = np.array([y1, y2, y3])
        self.coefficients = np.linalg.solve(m, n)
        self.a, self.b, self.c = self.coefficients[0], self.coefficients[1], self.coefficients[2]
        self.f = lambda x: self.a * x ** 2 + self.b * x + self.c


mac_top = Parabola(7, 5, 7.35, 23, 7.2, 11)
mac_bot = Parabola(7, 3, 7.4, 16, 7.3, 7)
arac_top = Parabola(7.15, 30, 7.35, 27, 7.25, 28)
arac_bot = Parabola(7.1, 26, 7.35, 23, 7.2, 25)

#crac_top = Parabola()
#crac_bot = Parabola()
#mal_top = Parabola()
#crac_bot = Parabola()
#aral_top = Parabola()
#crac_bot = Parabola()
#cral_top = Parabola()
#crac_bot = Parabola()

for p in [mac_top, mac_bot, arac_top, arac_bot]:
    print(p.coefficients, "     @ 7.25 -->", p.f(7.25))
