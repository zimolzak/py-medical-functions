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
# Source:
# https://upload.wikimedia.org/wikipedia/commons/1/18/Acid-base_nomogram.svg
# https://commons.wikimedia.org/wiki/File:Acid-base_nomogram.svg

A = [7.44, 31]
B = [7.46, 26]
C = [7.46, 20]
D = [7.4, 16]
E = [7.35, 23]
F = [7.35, 27]

# Naming extreme points of curves

MACT = [7, 5]
MACB = [7, 3]
ARACT = [7.15, 30]
ARACB = [7.1, 26]
CRACT = [7.325, 54]
CRACB = [7.2, 41]
MALT = [7.51, 54]
MALB = [7.625, 54]
ARALT = [7.73, 19]
ARALB = [7.61, 14]
CRALT = [7.5, 14]  # hard to read
CRALB = [7.45, 12]  # hard to read

mac_top = Parabola(MACT, E, [7.2, 11])
mac_bot = Parabola(MACB, D, [7.3, 7])

arac_top = Parabola(ARACT, F, [7.25, 28])
arac_bot = Parabola(ARACB, E, [7.2, 25])

crac_top = Parabola(CRACT, A, [7.4, 45])
crac_bot = Parabola(CRACB, F, [7.25, 35])

mal_top = Parabola(MALT, A, [7.5, 46])
mal_bot = Parabola(MALB, B, [7.6, 40])

aral_top = Parabola(ARALT, B, [7.6, 23])
aral_bot = Parabola(ARALB, C, [7.55, 17])

cral_top = Parabola(CRALT, C, [7.475, 16])  # hard to read
cral_bot = Parabola(CRALB, D, [7.42, 15])  # hard to read

for p in [mac_top, mac_bot, arac_top, arac_bot,
          crac_top, crac_bot, mal_top, mal_bot,
          aral_top, aral_bot, cral_top, cral_bot]:
    print(p.coefficients, "     @ 7.35 -->", p.f(7.35))
