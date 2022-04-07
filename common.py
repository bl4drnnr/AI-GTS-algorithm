def getRule(ruleName, ruleValue, allRules):
    return list(allRules[ruleName].keys())[list(allRules[ruleName].values()).index(ruleValue)]


def getTwoMaxValue(obj):
    return sorted(obj, key=lambda dct: list(dct.values())[0])[-2:]


def H(Epb, Ep, E):
    if Ep / Epb == 1:
        return "rule"
    return format((Epb / E) + (Ep / Epb) ** 0.5, ".3f")
