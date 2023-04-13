from meld import meld_no_rounding

na = 130.0
inr = 1.8
tb = 2.0
cr = 1.7

names = ["na ", "inr", "tb ", "cr "]

# Take smallest lab number, add 0.1, find out what fold increase that is.
delta_factor = (min(inr, cr, tb) + 0.1) / min(inr, cr, tb)
pct = round((delta_factor - 1) * 100, 1)
print(pct, "percent change in each lab increases MELD by:\n")

initial_conditions = (na, inr, tb, cr)
m1 = meld_no_rounding(*initial_conditions)

for i in range(4):
    conditions = list(initial_conditions)
    if i == 0:
        # for sodium a decrease is bad
        conditions[i] *= (1 - delta_factor)
    else:
        # for all others, increase is bad
        conditions[i] *= delta_factor
    m2 = meld_no_rounding(*conditions)
    dy = m2 - m1
    print(names[i], round(dy, 2))
