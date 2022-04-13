from parser import getData, getKeyAttribute, getAllPossibleAttributes
from collections import Counter
DATA = getData()
KEY_ATTRIBUTE = getKeyAttribute()
ALL_POSSIBLE_ATTRIBUTES = getAllPossibleAttributes()


def getRule(ruleName, ruleValue, allRules):
    return list(allRules[ruleName].keys())[list(allRules[ruleName].values()).index(ruleValue)]


def getXMaxValues(obj, n):
    maxValues = {}
    sortedRuleAttributes = sorted(obj, key=lambda x: max(v for v in x.values()))[-n:]
    for rule in sortedRuleAttributes:
        for attr, value in rule.items():
            maxValues[attr] = value
    return maxValues


def H(Epb, Ep, E):
    if Ep / Epb == 1:
        return "rule"
    return format((Epb / E) + (Ep / Epb) ** 0.5, ".3f")


def lookForComplicatedRules(currentRecord, maxValues):
    newRule = {}
    newRuleRecords = []
    for attr, value in maxValues.items():
        newRule[attr] = currentRecord[attr]
    for i, record in enumerate(DATA):
        quantityOfMatchAttributes = 0
        for attr, value in newRule.items():
            if record[attr] == newRule[attr]:
                quantityOfMatchAttributes += 1
        if quantityOfMatchAttributes == len(list(newRule)):
            newRuleRecords.append({i: record})

    outputData = [newRuleRecords, newRule]
    return outputData


def generateNewRule(GENERATED_RULES, currentRecord, maxValues, rulesAttributes, ITERATOR):
    newRule = "IF "
    newRecordsWithComplicatedRules = lookForComplicatedRules(currentRecord, maxValues)
    for attr, value in newRecordsWithComplicatedRules[1].items():
        newRule = newRule + str(attr) + " = "
        if list(newRecordsWithComplicatedRules[1])[-1] == attr:
            newRule = newRule + str(getRule(attr, value, ALL_POSSIBLE_ATTRIBUTES))
        else:
            newRule = newRule + str(getRule(attr, value, ALL_POSSIBLE_ATTRIBUTES)) + " AND "

    checkForRule = []
    for record in newRecordsWithComplicatedRules[0]:
        for attr, value in record.items():
            checkForRule.append(value[KEY_ATTRIBUTE])
    if Counter(checkForRule).most_common(1)[0][1] == len(checkForRule):
        newRule += " THEN {response} = {result}".format(
            response=KEY_ATTRIBUTE,
            result=getRule(KEY_ATTRIBUTE, Counter(checkForRule).most_common(1)[0][0], ALL_POSSIBLE_ATTRIBUTES)
        )
        for record in newRecordsWithComplicatedRules[0]:
            pushRule = True
            for rule in GENERATED_RULES:
                if rule['index'] == list(record)[0]:
                    pushRule = False
            if pushRule:
                # @TODO HERE SHOULD BE CHECK FOR DOUBLE RULE
                GENERATED_RULES.append({'index': list(record)[0], 'rule': newRule})
    else:
        newMaxValues = getXMaxValues(rulesAttributes, ITERATOR)
        ITERATOR += 1
        generateNewRule(GENERATED_RULES, currentRecord, newMaxValues, rulesAttributes, ITERATOR)

    return GENERATED_RULES


def printResults(GENERATED_RULES):
    listOfRules = {}
    for item in GENERATED_RULES:
        if listOfRules.get(item['rule']) is None:
            listOfRules[item['rule']] = [item['index'] + 1]
        else:
            listOfRules[item['rule']].append(item['index'] + 1)
        print('{index} - {rule}'.format(index=item['index'] + 1, rule=item['rule']))

    print('----------------------------------')
    print('LIST OF ALL RULES AND DEDICATED RECORDS TO THOSE RULES')

    for i, attr in enumerate(listOfRules.items()):
        print("{idx} - {rule} - {records}".format(idx=i+1, rule=attr[0], records=attr[1]))
