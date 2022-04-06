import json
from common import getRule, extractData, H


f = open('input.json')
data = json.load(f)

# createdRules = []
# attrsValues = []
inputDataLen = len(data['inputdata'])
# firstRecord = data['inputdata'][0]

for x in range(inputDataLen):
    totalQuantityOfAttr = 1
    totalQuantityOfMismatchAttr = 1
    currentRecord = data['inputdata'][x]
    for y in data['inputdata']:

        for iterate in range(4):
            if y[list(currentRecord)[iterate]] == currentRecord[list(currentRecord)[iterate]]:
                print(y[list(currentRecord)[iterate]])
                totalQuantityOfAttr += 1

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
#
# for rule in attrsValues:
#     for k, v in rule.items():
#         if "rule" in v:
#             createdRules.append("IF {rule} THEN {res}"
#                                 .format(rule=getRule(k, str(firstRecord[k])), res=getRule('socz', str(firstRecord['socz']))))
#