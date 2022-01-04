from math import log


def limit_lab(x, low=float('-inf'), hi=float('inf')):
    if x < low:
        return low
    elif x > hi:
        return hi
    return x


def na_correct(na):
    return limit_lab(na, 125, 137)


def cr_correct(cr):
    return limit_lab(cr, 1.0, 4.0)


def tb_inr_correct(tb):
    return limit_lab(tb, 1.0)


def meld_i(inr, tb, cr):
    return round((0.957 * log(cr_correct(cr)) +
                  0.378 * log(tb_inr_correct(tb)) +
                  1.120 * log(tb_inr_correct(inr)) + 0.643), 1) * 10


def meld(na, inr, tb, cr):
    m = meld_i(inr, tb, cr)
    n = na_correct(na)
    if m > 11:
        m = m + 1.32 * (137 - n) - (0.033 * m * (137 - n))
    return limit_lab(m, hi=40)
