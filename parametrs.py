from parser import getData, getKeyAttribute
DATA = getData()
KEY_ATTRIBUTE = getKeyAttribute()


def H(Epb, Ep, E):
    if Ep / Epb == 1:
        return "rule"
    return format((Epb / E) + (Ep / Epb) ** 0.5, ".3f")


def strength(Ep):
    return Ep


def accuracy(Ep, Eb):
    return format((Ep / (Ep + Eb)), ".3f")


def generality(Ep, Eb, E):
    return format(((Ep + Eb) / E), ".3f")


def specificity(Ep, Eclass):
    return format((Ep / Eclass), ".3f")


def support(Ep, E):
    return format((Ep / E), ".3f")


# TODO Problem with records that are duplicated
def compareRuleAndRecord(rule, record):
    res = False
    comparer = True
    for item in list(rule):
        if rule[item] != record[item]:
            comparer = False

    if not comparer and rule[KEY_ATTRIBUTE] == record[KEY_ATTRIBUTE]:
        res = True

    return res


def calculateAllDataPerRule(rule, q):
    E = len(DATA)
    Ep = q
    Eb = 0
    Eclass = 0

    for record in DATA:
        if compareRuleAndRecord(rule, record):
            Eb += 1
        if record[KEY_ATTRIBUTE] == rule[KEY_ATTRIBUTE]:
            Eclass += 1

    print("Rule's strength: " + str(strength(Ep)))
    print("Rule's accuracy: " + str(accuracy(Ep, Eb)))
    print("Rule's generality: " + str(generality(Ep, Eb, E)))
    print("Rule's specificity: " + str(specificity(Ep, Eclass)))
    print("Rule's support: " + str(support(Ep, E)))
