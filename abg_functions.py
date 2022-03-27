import numpy as np


class Parabola:
    coefficients: np.ndarray  # Python 3.5 doesn't like this
    a: float
    b: float
    c: float
    extreme_point: list
    vertex_point: list

    def __init__(self, p: list, q: list, r: list):
        """Define a parabolic curve from 3 points.

        Given points are x1,y1 .. x3,y3.
        Want to find coefficients a, b, c for general eqn y = a x^2 + b x + c .
        Do this by solving system (matrix eqn) M * x = n , which is a system of:
        (a * x1^2) + (b * x1) + (c * 1) = y1

        This class exposes several useful things:
        a function of the parabola, the coefficients, and the endpoints.

        :param p: extreme point of an ABG curve
        :param q: interior "vertex" point
        :param r: midpoint of an ABG curve
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


def cmp_func(y: float, behavior: str, f, x: float) -> bool:
    """Decide whether y < f(x), but where "<" can be specified.

    :param y: number to compare to f(x)
    :param behavior: string that can be 'less' or 'greater'
    :param f: function of 1 variable
    :param x: number at which to evaluate f, and then compare to y
    :return: boolean, whether or not y > f(x) or y < f(x) etc.
    """
    if behavior == 'less':
        return y < f(x)
    elif behavior == 'greater':
        return y > f(x)
    else:
        raise ValueError


def line_func(p1: list, p2: list):
    """Take two x,y points. Return a linear function through them both.

    :param p1: list of [x1, y1] ordered pair (point)
    :param p2: list of [x2, y2]
    :return: (linear) function in 1 variable, which passes through both points.
    """
    assert len(p1) == len(p2) == 2
    x1, y1, = p1
    x2, y2 = p2
    m = (y1 - y2) / (x1 - x2)  # let it raise error if x1 == x2
    return lambda x: m * (x - x1) + y1


class Region:
    vtx_behavior: str
    ext_behavior: str

    def __init__(self, top: Parabola, bottom: Parabola, ext_behavior: str, vtx_behavior: str):
        """Define a region from 2 Parabola objects.

        Parabola objects comprise a curve and 2 endpoints. When you link the extreme and vertex endpoints
        of 2 parabolas, you get a Region (which has curve-line-curve-line bounds).
        The _behavior parameters define whether the 2 linear boundaries have region below them or above them.
        In future we may calculate this; currently we specify.

        :param top: the parabola that makes up the upper edge of the ABG region
        :param bottom: parabola for the bottom edge of the region
        :param ext_behavior: pass to cmp_func() whether region is </> segment connecting extreme points of the parabolas
        :param vtx_behavior: whether the region is below/above the segment connecting the 2 vertex points
        """
        self.top_curve = top.f
        self.bottom_curve = bottom.f
        self.ext_line = line_func(top.extreme_point, bottom.extreme_point)
        self.vtx_line = line_func(top.vertex_point, bottom.vertex_point)
        self.ext_behavior = ext_behavior
        self.vtx_behavior = vtx_behavior

    def contains(self, point: list) -> bool:
        """Determine whether the Region object contains the specified point.

        :param point: list of point [x, y] usually pH and bicarbonate, respectively.
        :return: Boolean, whether the point is inside the region.
        """
        if len(point) != 2:
            raise IndexError
        x, y = point
        return self.bottom_curve(x) < y < self.top_curve(x) and \
            cmp_func(y, self.ext_behavior, self.ext_line, x) and \
            cmp_func(y, self.vtx_behavior, self.vtx_line, x)


class RegionQuad:
    def __init__(self, p1: list, p2: list, p3: list, p4: list):
        """Define a quadrilateral region.

        p1 p2 p3 must define the top edges.
        p3 p4 p1 must define the bottom edges.

                   p2
             p1          p3
                   p4

        :param p1: Start of one upper segment
        :param p2: End of 1st upper seg, start of 2nd upper
        :param p3: End of 2nd upper, start of 1st bottom seg.
        :param p4: End of 1st bottom seg, start of 2nd bottom
        """
        self.top12 = line_func(p1, p2)
        self.top23 = line_func(p2, p3)
        self.bot34 = line_func(p3, p4)
        self.bot41 = line_func(p4, p1)

    def contains(self, point: list) -> bool:
        if len(point) != 2:
            raise IndexError
        x, y = point
        return self.top12(x) > y > self.bot34(x) and \
            self.top23(x) > y > self.bot41(x)


class RegionSimple:
    def __init__(self, xmin, xmax, ymin, ymax):
        if xmin >= xmax or ymin >= ymax:
            raise ValueError
        self.xmin = xmin
        self.xmax = xmax
        self.ymin = ymin
        self.ymax = ymax

    def contains(self, point: list) -> bool:
        if len(point) != 2:
            raise IndexError
        x, y = point
        return self.xmin <= x <= self.xmax and \
            self.ymin <= y <= self.ymax
