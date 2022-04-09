import json

f = open('input.json')
DATA = json.load(f)
DATA = DATA['inputdata']
ALL_POSSIBLE_ATTRIBUTES = {}


def getData():
    return DATA


def getAllPossibleAttributes():
    return ALL_POSSIBLE_ATTRIBUTES


def getKeyAttribute():
    return list(DATA[0])[-1]


def getDecisionAttributes():
    decisionAttributes = {}
    for item in list(DATA[0])[:-1]:
        decisionAttributes[item] = 0
    return decisionAttributes


def parseInputData():
    # Get all possible attributes and classes
    for item in DATA:
        for attr, value in item.items():
            if ALL_POSSIBLE_ATTRIBUTES.get(attr) is None:
                ALL_POSSIBLE_ATTRIBUTES[attr] = {value: 0}
            else:
                if ALL_POSSIBLE_ATTRIBUTES[attr].get(value) is None:
                    ALL_POSSIBLE_ATTRIBUTES[attr][value] = 0
    # Parse those attributes and classes and give values
    for param in ALL_POSSIBLE_ATTRIBUTES:
        i = 0
        for attr, value in ALL_POSSIBLE_ATTRIBUTES[param].items():
            ALL_POSSIBLE_ATTRIBUTES[param][attr] += i
            i += 1
    # Parse input DATA
    for item in DATA:
        for attr, value in item.items():
            item[attr] = ALL_POSSIBLE_ATTRIBUTES[attr][value]
    return DATA
