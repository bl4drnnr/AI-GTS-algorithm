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
            # @TODO Fix index and push method just to make it easy then to sort and fix
            generatedRules.append({x: "IF {rule} = {condition} THEN {response} = {result}"
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
    if not ruleWasGenerated:
        newRule = "IF "
        newRecordsWithComplicatedRules = lookForComplicatedRules(currentRecord, twoMaxValues)
        # Generate complicated rule
        for attr, value in newRecordsWithComplicatedRules[1].items():
            newRule = newRule + str(attr) + " = "
            if list(newRecordsWithComplicatedRules[1])[-1] == attr:
                newRule = newRule + str(getRule(attr, value, allPossibleAttributes))
            else:
                newRule = newRule + str(getRule(attr, value, allPossibleAttributes)) + " AND "

        checkForRule = []
        for t in newRecordsWithComplicatedRules[0]:
            print(t)
            for attr, value in t.items():
                checkForRule.append(value[keyAttribute])
        print("checkForRule: " + str(checkForRule))
        newRule += " THEN {response} = {result}".format(
            response=keyAttribute, result=getRule(keyAttribute, Counter(checkForRule).most_common(1)[0][0], allPossibleAttributes)
        )
        print("newRule: " + str(newRule))
    nonRulesAttributes = []
    # Iterate one more time input data, but with 1+ conditions
    # Recount my calcs, because it looks like something went wrong

    # if inputDataLength == len(generatedRules):
    #     print("Stop, all rules has been generated!")
    print('#####################')


for item in generatedRules:
    for attr, value in item.items():
        print("{key} - {value}".format(key=attr+1, value=value))
