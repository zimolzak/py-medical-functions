import numpy as np


class Parabola:
    def __init__(self, p, q, r):
        """Define a parabolic curve from 3 points.

        Given points are x1,y1 .. x3,y3.
        Want to find coeffs a, b, c for general eqn y = a x^2 + b x + c .
        Do this by solving system (matrix eqn) M * x = n , which is a system of
        (a * x1^2) + (b * x1) + (c * 1) = y1
        """

        x1, y1 = p
        x2, y2 = q
        x3, y3 = r

        m = np.array([[x1 ** 2, x1, 1],
                      [x2 ** 2, x2, 1],
                      [x3 ** 2, x3, 1]])
        n = np.array([y1, y2, y3])
        self.coefficients = np.linalg.solve(m, n)
        self.a, self.b, self.c = self.coefficients[0], self.coefficients[1], self.coefficients[2]
        self.f = lambda x: self.a * x ** 2 + self.b * x + self.c


# I'm naming the "vertex" points where 2 curves meet, clockwise, A-F, starting at 12 o'clock.

A = [7.44, 31]
B = None
C = None
D = [7.4, 16]
E = [7.35, 23]
F = [7.35, 27]

# Naming extreme points of curves

MACT = [7, 5]
MACB = [7, 3]
ARACT = [7.15, 30]
ARACB = [7.1, 26]
CRACT = None
CRACB = None
MALT = None
MALB = None
ARALT = None
ARALB = None
CRALT = None
CRALB = None


mac_top = Parabola(MACT, E, [7.2, 11])
mac_bot = Parabola(MACB, D, [7.3, 7])
arac_top = Parabola(ARACT, F, [7.25, 28])
arac_bot = Parabola(ARACB, E, [7.2, 25])

#crac_top = Parabola(CRACT, )
#crac_bot = Parabola(CRACB, )

#mal_top = Parabola(MALT, )
#mal_bot = Parabola(MALB, )

#aral_top = Parabola(ARALT, )
#aral_bot = Parabola(ARALB, )

#cral_top = Parabola(CRALT, )
#cral_bot = Parabola(CRALB, )

for p in [mac_top, mac_bot, arac_top, arac_bot]:
    print(p.coefficients, "     @ 7.25 -->", p.f(7.25))
