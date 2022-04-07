import json

f = open('input.json')
data = json.load(f)
data = data['inputdata']
allPossibleAttributes = {}


def getAllPossibleAttributes():
    return allPossibleAttributes


def getKeyAttribute():
    return list(data[0])[-1]


def getDecisionAttributes():
    decisionAttributes = {}
    for item in list(data[0])[:-1]:
        decisionAttributes[item] = 0
    return decisionAttributes


def parseInputData():
    # Get all possible attributes and classes
    for item in data:
        for attr, value in item.items():
            if allPossibleAttributes.get(attr) is None:
                allPossibleAttributes[attr] = {value: 0}
            else:
                if allPossibleAttributes[attr].get(value) is None:
                    allPossibleAttributes[attr][value] = 0
    # Parse those attributes and classes and give values
    for param in allPossibleAttributes:
        i = 0
        for attr, value in allPossibleAttributes[param].items():
            allPossibleAttributes[param][attr] += i
            i += 1
    # Parse input data
    for item in data:
        for attr, value in item.items():
            item[attr] = allPossibleAttributes[attr][value]
    return data
