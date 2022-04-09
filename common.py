from parser import getData, getKeyAttribute, getAllPossibleAttributes
from collections import Counter
data = getData()
keyAttribute = getKeyAttribute()
allPossibleAttributes = getAllPossibleAttributes()


def getRule(ruleName, ruleValue, allRules):
    return list(allRules[ruleName].keys())[list(allRules[ruleName].values()).index(ruleValue)]


def getXMaxValues(obj, x):
    twoMaxValue = {}
    sortedNonRuleAttributes = sorted(obj, key=lambda dct: list(dct.values())[0])[-x:]
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


def generateNewRule(generatedRules, currentRecord, twoMaxValues):
    newRule = "IF "
    newRecordsWithComplicatedRules = lookForComplicatedRules(currentRecord, twoMaxValues)
    for attr, value in newRecordsWithComplicatedRules[1].items():
        newRule = newRule + str(attr) + " = "
        if list(newRecordsWithComplicatedRules[1])[-1] == attr:
            newRule = newRule + str(getRule(attr, value, allPossibleAttributes))
        else:
            newRule = newRule + str(getRule(attr, value, allPossibleAttributes)) + " AND "

    checkForRule = []
    for t in newRecordsWithComplicatedRules[0]:
        for attr, value in t.items():
            checkForRule.append(value[keyAttribute])
    print("checkForRule: " + str(checkForRule))
    print("checkForRule most common: " + str(Counter(checkForRule).most_common(1)))
    if Counter(checkForRule).most_common(1)[0][1] == len(checkForRule):
        newRule += " THEN {response} = {result}".format(
            response=keyAttribute,
            result=getRule(keyAttribute, Counter(checkForRule).most_common(1)[0][0], allPossibleAttributes)
        )
        for t in newRecordsWithComplicatedRules[0]:
            pushRule = True
            for rule in generatedRules:
                if rule['index'] == list(t)[0]:
                    pushRule = False
            if pushRule:
                generatedRules.append({'index': list(t)[0], 'rule': newRule})
    else:
        # From here I should continue
        print("Seems impossible to generate rule with this data!")

    return generatedRules
