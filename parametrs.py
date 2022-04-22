from parser import getData, getAllPossibleAttributes, getKeyAttribute, getDecisionAttributes
DATA = getData()
KEY_ATTRIBUTE = getKeyAttribute()


def H(Epb, Ep, E):
    if Ep / Epb == 1:
        return "rule"
    return format((Epb / E) + (Ep / Epb) ** 0.5, ".3f")


# Siła
def strength(Ep):
    return Ep


# Dokładność
def accuracy(Ep, Eb):
    return format((Ep / (Ep + Eb)), ".3f")


# Ogólność
def generality(Ep, Eb, E):
    return format(((Ep + Eb) / E), ".3f")


# Specyficzność
def specificity(Ep, Eclass):
    return format((Ep / Eclass), ".3f")


# Wsparcie
def support(Ep, E):
    return format((Ep / E), ".3f")


def calculateAllDataPerRule(rule, q):
    E = len(DATA)
    Ep = q
    Eb = 0
    Eclass = 0

    for record in DATA:
        recordCorrection = True
        for attr, value in rule.items():
            print('sad')
        if recordCorrection:
            Eb += 1

    print("Rule's strength: " + str(strength(Ep)))
    print("Rule's accuracy: " + str(accuracy(Ep, Eb)))
