def convert_usa(x):
    if x > 0:
        frac = x/100
    else:
        frac = (-100 / x)

    dec = frac + 1
    prob = 1 / dec

    print(x, 'dec=', dec, '    frac=', frac, ':1     prob=', prob)


for k, v in {'unc': 160, 'duke': -190}.items():
    print(k, ':   ', end='')
    convert_usa(v)
