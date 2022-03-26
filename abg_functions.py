import numpy as np


class Parabola:
    def __init__(self, p: list, q: list, r: list):
        """Define a parabolic curve from 3 points.

        Given points are x1,y1 .. x3,y3.
        Want to find coeffs a, b, c for general eqn y = a x^2 + b x + c .
        Do this by solving system (matrix eqn) M * x = n , which is a system of
        (a * x1^2) + (b * x1) + (c * 1) = y1

        p should be extreme point of an ABG curve
        q should be an interior "vertex" point
        r should be midpoint
        """

        if len(p) != len(q) != len(r) != 2:
            raise ValueError

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


def cmp_func(y: float, behavior: str, f, x: float):
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
        return self.bottom_curve(x) < y < self.top_curve(x) and \
            cmp_func(y, self.ext_behavior, self.ext_line, x) and \
            cmp_func(y, self.vtx_behavior, self.vtx_line, x)
