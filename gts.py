import json
from common import getRule, getTwoMaxValue, H
from parser import parseInputData

f = open('input.json')
data = json.load(f)

inputDataLength = len(data['inputdata'])
generatedRules = []

for x in range(inputDataLength):
    currentRecord = data['inputdata'][x]
    currentRecordData = {
        "wiek": 0,
        "wada": 0,
        "ast": 0,
        "lz": 0,
    }
    currentRecordDataFiltered = {
        "wiek": 0,
        "wada": 0,
        "ast": 0,
        "lz": 0,
    }

    # Collecting information for one current record
    for y in data['inputdata']:
        for iterator in range(4):
            if y[list(currentRecord)[iterator]] == currentRecord[list(currentRecord)[iterator]]:
                currentRecordData[list(currentRecord)[iterator]] += 1
                currentRecordDataFiltered[list(currentRecord)[iterator]] += 1

    # Filter collected data to count values of G, A and H
    for z in data['inputdata']:
        if z['socz'] == currentRecord['socz']:
            for iterator in range(4):
                if currentRecord[list(currentRecord)[iterator]] == z[list(currentRecord)[iterator]]:
                    currentRecordDataFiltered[list(currentRecord)[iterator]] -= 1

    # Check if there is already generated rule
    print("currentRecordData: " + str(currentRecordData))
    print("currentRecordDataFiltered: " + str(currentRecordDataFiltered))
    print("currentRecord: " + str(currentRecord))
    nonRulesAttributes = []
    for rule in range(4):
        quantityOfRightRecords = \
            currentRecordData[list(currentRecordData)[rule]] - \
            currentRecordDataFiltered[list(currentRecordDataFiltered)[rule]]
        quantityOfAllThisTypeRecords = currentRecordData[list(currentRecordData)[rule]]
        generatedRule = H(quantityOfAllThisTypeRecords, quantityOfRightRecords, inputDataLength)
        if generatedRule == "rule":
            generatedRules.append({x: "IF {condition} THEN {response}"
                .format(
                    condition=getRule(list(currentRecordData)[rule], currentRecord[list(currentRecord)[rule]]),
                    response=getRule("socz", currentRecord["socz"]),
                    )})
            print(list(currentRecordData)[rule] + " rule ")
        else:
            nonRulesAttributes.append({list(currentRecordData)[rule]: generatedRule})
            print(list(currentRecordData)[rule] + " not rule :( " + str(generatedRule))

    print("nonRulesAttributes: " + str(nonRulesAttributes))
    twoMaxValues = getTwoMaxValue(nonRulesAttributes)
    print("twoMaxValues: " + str(twoMaxValues))
    nonRulesAttributes = []
    # Iterate one more time input data, but with 1+ conditions

    # if inputDataLength == len(generatedRules):
    #     print("Stop, all rules has been generated!")
    print('#####################')

for item in generatedRules:
    for attr, value in item.items():
        print("{key} - {value}".format(key=attr+1, value=value))
    # print('-------------')
