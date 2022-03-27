from abg_functions import Region, Parabola, RegionQuad

# Naming the "vertex" points where 2 curves meet, clockwise, A-F, starting at 12 o'clock.

# Source:
# https://upload.wikimedia.org/wikipedia/commons/1/18/Acid-base_nomogram.svg
# https://commons.wikimedia.org/wiki/File:Acid-base_nomogram.svg

A = [7.44, 31]
B = [7.461, 26]
C = [7.46, 20]  # NEARLY directly below B
D = [7.41, 17]
E = [7.35, 23]
F = [7.351, 27]  # NEARLY directly above E

# Naming extreme points of curves

MACT = [7.001, 5]
MACB = [7, 3]  # directly below
ARACT = [7.15, 30]
ARACB = [7.1, 26]
CRACT = [7.325, 54]
CRACB = [7.2, 41]
MALT = [7.51, 54]
MALB = [7.625, 54]
ARALT = [7.73, 19]
ARALB = [7.61, 14]
CRALT = [7.485, 14]
CRALB = [7.44, 13]

# Make the curves themselves

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

# Regions
met_acidosis_reg = Region(mac_top, mac_bot, 'less', 'less')
acute_resp_acidosis_reg = Region(arac_top, arac_bot, 'less', 'greater')
chronic_resp_acidosis_reg = Region(crac_top, crac_bot, 'less', 'greater')
met_alkalosis_reg = Region(mal_top, mal_bot, 'less', 'greater')
acute_resp_alkalosis_reg = Region(aral_top, aral_bot, 'greater', 'less')
chronic_resp_alkalosis_reg = RegionQuad(D, C, CRALT, CRALB)

REGION_DICT = {'mac': met_acidosis_reg, 'arac': acute_resp_acidosis_reg,
             'crac': chronic_resp_acidosis_reg, 'malk': met_alkalosis_reg,
             'aralk': acute_resp_alkalosis_reg, 'cralk': chronic_resp_alkalosis_reg}
