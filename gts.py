import json
from common import getRule, extractData, H

f = open('input.json')
data = json.load(f)

inputDataLen = len(data['inputdata'])

for x in range(inputDataLen):
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

# see docs
# fix iterations
# for _ in range(inputDataLen):
#     for iterate in range(4):
#         totalQuantityOfAttr = 1
#         totalQuantityOfMismatchAttr = 1
#         test = {}
#         for i in data['inputdata'][1:]:
#
#             if i[list(firstRecord)[iterate]] == firstRecord[list(firstRecord)[iterate]]:
#                 totalQuantityOfAttr += 1
#
#             if i[list(firstRecord)[iterate]] == firstRecord[list(firstRecord)[iterate]] \
#                     and i['socz'] == firstRecord['socz']:
#                 totalQuantityOfMismatchAttr += 1
#
#         test[list(firstRecord)[iterate]] = H(totalQuantityOfAttr, totalQuantityOfMismatchAttr, inputDataLen)
#         print(test)
#         attrsValues.append(test)
#         test = {}

# for rule in attrsValues:
#     for k, v in rule.items():
#         if "rule" in v:
#             createdRules.append("IF {rule} THEN {res}"
#                                 .format(rule=getRule(k, str(firstRecord[k])), res=getRule('socz', str(firstRecord['socz']))))
#
