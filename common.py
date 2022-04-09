from parser import getData, getKeyAttribute, getAllPossibleAttributes
from collections import Counter
DATA = getData()
KEY_ATTRIBUTE = getKeyAttribute()
ALL_POSSIBLE_ATTRIBUTES = getAllPossibleAttributes()


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
    for i, record in enumerate(DATA):
        quantityOfMatchAttributes = 0
        for attr, value in newRule.items():
            if record[attr] == newRule[attr]:
                quantityOfMatchAttributes += 1
        if quantityOfMatchAttributes == len(list(newRule)):
            newRuleRecords.append({i+1: record})

    outputData.append(newRuleRecords)
    outputData.append(newRule)
    return outputData


def generateNewRule(GENERATED_RULES, currentRecord, twoMaxValues, nonRulesAttributes, ITERATOR):
    newRule = "IF "
    newRecordsWithComplicatedRules = lookForComplicatedRules(currentRecord, twoMaxValues)
    for attr, value in newRecordsWithComplicatedRules[1].items():
        newRule = newRule + str(attr) + " = "
        if list(newRecordsWithComplicatedRules[1])[-1] == attr:
            newRule = newRule + str(getRule(attr, value, ALL_POSSIBLE_ATTRIBUTES))
        else:
            newRule = newRule + str(getRule(attr, value, ALL_POSSIBLE_ATTRIBUTES)) + " AND "

    checkForRule = []
    for t in newRecordsWithComplicatedRules[0]:
        for attr, value in t.items():
            checkForRule.append(value[KEY_ATTRIBUTE])
    print("checkForRule: " + str(checkForRule))
    print("checkForRule most common: " + str(Counter(checkForRule).most_common(1)))
    if Counter(checkForRule).most_common(1)[0][1] == len(checkForRule):
        newRule += " THEN {response} = {result}".format(
            response=KEY_ATTRIBUTE,
            result=getRule(KEY_ATTRIBUTE, Counter(checkForRule).most_common(1)[0][0], ALL_POSSIBLE_ATTRIBUTES)
        )
        for t in newRecordsWithComplicatedRules[0]:
            pushRule = True
            for rule in GENERATED_RULES:
                if rule['index'] == list(t)[0]:
                    pushRule = False
            # Something with this check
            if pushRule:
                GENERATED_RULES.append({'index': list(t)[0], 'rule': newRule})
    else:
        newMaxValues = getXMaxValues(nonRulesAttributes, ITERATOR)
        ITERATOR += 1
        # From here I should continue
        generateNewRule(GENERATED_RULES, currentRecord, newMaxValues, nonRulesAttributes)
        print("Seems impossible to generate rule with this DATA!")

    outputData = [GENERATED_RULES, ITERATOR]
    return outputData

