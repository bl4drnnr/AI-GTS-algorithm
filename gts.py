from collections import Counter
from common import getRule, getTwoMaxValues, lookForComplicatedRules, H
from parser import parseInputData, getAllPossibleAttributes, getKeyAttribute, getDecisionAttributes
data = parseInputData()
keyAttribute = getKeyAttribute()
allPossibleAttributes = getAllPossibleAttributes()

inputDataLength = len(data)
generatedRules = []

for x in range(inputDataLength):
    currentRecord = data[x]
    currentRecordData = getDecisionAttributes()
    currentRecordDataFiltered = getDecisionAttributes()

    # Collecting information for one current record
    for y in data:
        for iterator in range(len(list(getDecisionAttributes()))):
            if y[list(currentRecord)[iterator]] == currentRecord[list(currentRecord)[iterator]]:
                currentRecordData[list(currentRecord)[iterator]] += 1
                currentRecordDataFiltered[list(currentRecord)[iterator]] += 1

    # Filter collected data to count values of G, A and H
    for z in data:
        if z[keyAttribute] == currentRecord[keyAttribute]:
            for iterator in range(len(list(getDecisionAttributes()))):
                if currentRecord[list(currentRecord)[iterator]] == z[list(currentRecord)[iterator]]:
                    currentRecordDataFiltered[list(currentRecord)[iterator]] -= 1

    # Check if there is already generated rule
    print("currentRecordData: " + str(currentRecordData))
    print("currentRecordDataFiltered: " + str(currentRecordDataFiltered))
    print("currentRecord: " + str(currentRecord))
    nonRulesAttributes = []
    ruleWasGenerated = False
    for rule in range(len(list(getDecisionAttributes()))):
        quantityOfRightRecords = \
            currentRecordData[list(currentRecordData)[rule]] - \
            currentRecordDataFiltered[list(currentRecordDataFiltered)[rule]]
        quantityOfAllThisTypeRecords = currentRecordData[list(currentRecordData)[rule]]
        generatedRule = H(quantityOfAllThisTypeRecords, quantityOfRightRecords, inputDataLength)
        if generatedRule == "rule":
            generatedRules.append({
                'index': x,
                'rule': "IF {rule} = {condition} THEN {response} = {result}"
                .format(
                    rule=list(currentRecordData)[rule],
                    condition=getRule(list(currentRecordData)[rule], currentRecord[list(currentRecord)[rule]], allPossibleAttributes),
                    response=keyAttribute,
                    result=getRule(keyAttribute, currentRecord[keyAttribute], allPossibleAttributes)
                    )})
            ruleWasGenerated = True
            print(list(currentRecordData)[rule] + " - rule")
        else:
            nonRulesAttributes.append({list(currentRecordData)[rule]: generatedRule})
            print(list(currentRecordData)[rule] + " - not rule :( - " + str(generatedRule))

    print("nonRulesAttributes: " + str(nonRulesAttributes))
    twoMaxValues = getTwoMaxValues(nonRulesAttributes)
    # Generate complicated rule
    if not ruleWasGenerated:
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
                response=keyAttribute, result=getRule(keyAttribute, Counter(checkForRule).most_common(1)[0][0], allPossibleAttributes)
            )
            for t in newRecordsWithComplicatedRules[0]:
                pushRule = True
                for rule in generatedRules:
                    if rule['index'] == list(t)[0]:
                        pushRule = False
                if pushRule:
                    generatedRules.append({
                        'index': list(t)[0],
                        'rule': newRule
                    })
            # Push here
        else:
            print("Seems impossible to generate rule with this data!")
        print("newRule: " + str(newRule))
    nonRulesAttributes = []
    # Recount my calcs, because it looks like something went wrong
    print('#####################')


for item in generatedRules:
    print('{index} - {rule}'.format(index=item['index'], rule=item['rule']))
