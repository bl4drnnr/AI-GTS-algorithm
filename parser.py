import json

f = open('input2.json')
data = json.load(f)
data = data['inputdata']
decisionAttribute = list(data[0])[-1]
conditionalAttributes = list(data[0])[0:len(list(data[0])) - 1]


def parseInputData(inputData):
    return