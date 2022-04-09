from parser import parseInputData
data = parseInputData()


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
    print('---------------------')
    print("currentRecords: " + str(currentRecord))
    print("twoMaxValues: " + str(twoMaxValues))
    newRule = {}
    newRuleRecords = []
    outputData = []
    for attr, value in twoMaxValues.items():
        newRule[attr] = currentRecord[attr]
    print("newRule: " + str(newRule))
    print('---------------------')
    for i, record in enumerate(data):
        quantityOfMatchAttributes = 0
        for attr, value in newRule.items():
            if record[attr] == newRule[attr]:
                quantityOfMatchAttributes += 1
        if quantityOfMatchAttributes == len(list(newRule)):
            newRuleRecords.append({i+1: record})

    outputData.append(newRuleRecords)
    outputData.append(newRule)
    return outputData
