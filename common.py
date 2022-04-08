def getRule(ruleName, ruleValue, allRules):
    return list(allRules[ruleName].keys())[list(allRules[ruleName].values()).index(ruleValue)]


def getTwoMaxValue(obj):
    twoMaxValue = {}
    sortedNonRuleAttributes = sorted(obj, key=lambda dct: list(dct.values())[0])[-2:]
    for item in sortedNonRuleAttributes:
        for attr, value in item.items():
            twoMaxValue[attr] = value
    return twoMaxValue



def H(Epb, Ep, E):
    if Ep / Epb == 1:
        return "rule"
    return format((Epb / E) + (Ep / Epb) ** 0.5, ".3f")


def lookForComplicatedRules(currentRecords, twoMaxValues):
    newRule = {}
    print('---------------------')
    print("currentRecords: " + str(currentRecords))
    print("twoMaxValues: " + str(twoMaxValues))
