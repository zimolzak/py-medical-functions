import numpy as np


class Parabola:
    def __init__(self, p, q, r):
        """Define a parabolic curve from 3 points.

        Given points are x1,y1 .. x3,y3.
        Want to find coeffs a, b, c for general eqn y = a x^2 + b x + c .
        Do this by solving system (matrix eqn) M * x = n , which is a system of
        (a * x1^2) + (b * x1) + (c * 1) = y1

        p should be extreme point of an ABG curve
        q should be an interior "vertex" point
        r should be midpoint
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
        self.extreme_point = p
        self.vertex_point = q


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
CRALT = [7.5, 14]  # fixme - hard to read on the diagram
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


def cmp_func(y, behavior, f, x):
    if behavior == 'less':
        return y < f(x)
    elif behavior == 'greater':
        return y > f(x)
    elif behavior == 'ignore':
        return True  # fixme - might be wrong to do it this way
    else:
        raise ValueError


def line_func(p1: list, p2: list):
    assert len(p1) == len(p2) == 2
    x1, y1, = p1
    x2, y2 = p2
    if x1 == x2:
        return lambda x: np.inf  # fixme - does it have to be +/- inf?
    else:
        m = (y1 - y2) / (x1 - x2)
        return lambda x: m * (x - x1) + y1


class Region:
    def __init__(self, top: Parabola, bottom: Parabola, ext_behavior: str, vtx_behavior: str):
        self.top_curve = top.f
        self.bottom_curve = bottom.f
        self.ext_line = line_func(top.extreme_point, bottom.extreme_point)
        self.vtx_line = line_func(top.vertex_point, bottom.vertex_point)
        self.ext_behavior = ext_behavior
        self.vtx_behavior = vtx_behavior

    def contains(self, point: list):
        if len(point) != 2:
            raise IndexError
        x, y = point
        return self.bottom_curve(x) < y < self.top_curve(x) and\
            cmp_func(y, self.ext_behavior, self.ext_line, x) and\
            cmp_func(y, self.vtx_behavior, self.vtx_line, x)


# fixme - not sure if the ones marked 'ignore' should be that way
met_acidosis_reg = Region(mac_top, mac_bot, 'ignore', 'less')
acute_resp_acidosis_reg = Region(arac_top, arac_bot, 'less', 'ignore')
chronic_resp_acidosis_reg = Region(crac_top, crac_bot, 'less', 'greater')
met_alkalosis_reg = Region(mal_top, mal_bot, 'less', 'greater')
acute_resp_alkalosis_reg = Region(aral_top, aral_bot, 'greater', 'ignore')
chronic_resp_alkalosis_reg = Region(cral_top, cral_bot, 'greater', 'less')

print("t", met_acidosis_reg.contains([7.2, 8]))  # fixme - turn this into a test
print("t", acute_resp_acidosis_reg.contains([7.125, 27]))
print("f", acute_resp_acidosis_reg.contains([7.11, 28]))  # expect false
print("t", chronic_resp_acidosis_reg.contains([7.35, 36]))
print("t", met_alkalosis_reg.contains([7.55, 40]))
print("t", acute_resp_alkalosis_reg.contains([7.6, 20]))
print("t", chronic_resp_alkalosis_reg.contains([7.45, 16]))
print()

REGION_DICT = {'mac': met_acidosis_reg, 'arac': acute_resp_acidosis_reg, 'crac': chronic_resp_acidosis_reg,
               'malk': met_acidosis_reg, 'aralk': acute_resp_alkalosis_reg, 'cralk': chronic_resp_alkalosis_reg}


def interpret(ph, bicarb, d=None):
    if d is None:
        d = REGION_DICT
    answers = {}
    for k, region in d.items():
        answers[k] = region.contains([ph, bicarb])
    return answers


print("norm ", interpret(7.4, 24))  # normal fixme - "ignore" should test x < > vertical line?
print("mac  ", interpret(7.2, 8))  # mac
print("arac ", interpret(7.125, 27))  # arac
print("extre", interpret(7.11, 28))  # extreme
print("crac ", interpret(7.35, 36))  # crac
print("malk ", interpret(7.55, 40))  # malk fixme does not detect
print("aralk", interpret(7.6, 20))  # aralk fixme 3 answers
print("cralk", interpret(7.45, 16))  # cralk
