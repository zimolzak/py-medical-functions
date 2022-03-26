from abg_interpreter import Region, Parabola, interpret

D = [7.4, 16]
E = [7.35, 23]
MACT = [7, 5]
MACB = [7, 3]
mac_top = Parabola(MACT, E, [7.2, 11])
mac_bot = Parabola(MACB, D, [7.3, 7])
met_acidosis_reg = Region(mac_top, mac_bot, 'ignore', 'less')


def test_region():
    assert met_acidosis_reg.contains([7.2, 8])
