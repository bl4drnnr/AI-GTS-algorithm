from common import getRule, getXMaxValues, generateNewRule, H
from parser import parseInputData, getAllPossibleAttributes, getKeyAttribute, getDecisionAttributes
DATA = parseInputData()
KEY_ATTRIBUTE = getKeyAttribute()
ALL_POSSIBLE_ATTRIBUTES = getAllPossibleAttributes()
ITERATOR = 2
INPUT_DATA_LENGTH = len(DATA)
GENERATED_RULES = []

for x in range(INPUT_DATA_LENGTH):
    currentRecord = DATA[x]
    currentRecordData = getDecisionAttributes()
    currentRecordDataFiltered = getDecisionAttributes()

    # Collecting information for one current record
    for y in DATA:
        for ITERATOR in range(len(list(getDecisionAttributes()))):
            if y[list(currentRecord)[ITERATOR]] == currentRecord[list(currentRecord)[ITERATOR]]:
                currentRecordData[list(currentRecord)[ITERATOR]] += 1
                currentRecordDataFiltered[list(currentRecord)[ITERATOR]] += 1

    # Filter collected DATA to count values of G, A and H
    for z in DATA:
        if z[KEY_ATTRIBUTE] == currentRecord[KEY_ATTRIBUTE]:
            for ITERATOR in range(len(list(getDecisionAttributes()))):
                if currentRecord[list(currentRecord)[ITERATOR]] == z[list(currentRecord)[ITERATOR]]:
                    currentRecordDataFiltered[list(currentRecord)[ITERATOR]] -= 1

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
        generatedRule = H(quantityOfAllThisTypeRecords, quantityOfRightRecords, INPUT_DATA_LENGTH)
        if generatedRule == "rule":
            GENERATED_RULES.append({
                'index': x,
                'rule': "IF {rule} = {condition} THEN {response} = {result}"
                .format(
                    rule=list(currentRecordData)[rule],
                    condition=getRule(list(currentRecordData)[rule], currentRecord[list(currentRecord)[rule]], ALL_POSSIBLE_ATTRIBUTES),
                    response=KEY_ATTRIBUTE,
                    result=getRule(KEY_ATTRIBUTE, currentRecord[KEY_ATTRIBUTE], ALL_POSSIBLE_ATTRIBUTES)
                    )})
            ruleWasGenerated = True
            print(list(currentRecordData)[rule] + " - rule")
        else:
            nonRulesAttributes.append({list(currentRecordData)[rule]: generatedRule})
            print(list(currentRecordData)[rule] + " - not rule :( - " + str(generatedRule))

    print("nonRulesAttributes: " + str(nonRulesAttributes))
    twoMaxValues = getXMaxValues(nonRulesAttributes, ITERATOR)
    # Generate complicated rule
    if not ruleWasGenerated:
        GENERATED_RULES = generateNewRule(GENERATED_RULES, currentRecord, twoMaxValues, nonRulesAttributes, ITERATOR)
        GENERATED_RULES = GENERATED_RULES[0]
        ITERATOR = GENERATED_RULES[1]
    nonRulesAttributes = []
    # Recount my calcs, because it looks like something went wrong
    print('#####################')


GENERATED_RULES = sorted(GENERATED_RULES, key=lambda ruleSort: ruleSort['index'])


for item in GENERATED_RULES:
    print('{index} - {rule}'.format(index=item['index'], rule=item['rule']))
