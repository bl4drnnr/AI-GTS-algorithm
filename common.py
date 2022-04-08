def getRule(ruleName, ruleValue, allRules):
    return list(allRules[ruleName].keys())[list(allRules[ruleName].values()).index(ruleValue)]


def getTwoMaxValues(obj):
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


def lookForComplicatedRules(currentRecord, twoMaxValues):
    newRule = {}
    for attr, value in currentRecord.items():
        for at, vl in twoMaxValues.items():
            if attr == at:
                newRule[attr] = value
    print('---------------------')
    print("currentRecords: " + str(currentRecord))
    print("twoMaxValues: " + str(twoMaxValues))
    print("newRule: " + str(newRule))
