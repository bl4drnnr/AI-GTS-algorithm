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
    for record in DATA:
        for ITERATOR in range(len(list(getDecisionAttributes()))):
            if record[list(currentRecord)[ITERATOR]] == currentRecord[list(currentRecord)[ITERATOR]]:
                currentRecordData[list(currentRecord)[ITERATOR]] += 1
                currentRecordDataFiltered[list(currentRecord)[ITERATOR]] += 1

    # Filter collected data to count values of G, A and H
    for record in DATA:
        if record[KEY_ATTRIBUTE] == currentRecord[KEY_ATTRIBUTE]:
            for ITERATOR in range(len(list(getDecisionAttributes()))):
                if currentRecord[list(currentRecord)[ITERATOR]] == record[list(currentRecord)[ITERATOR]]:
                    currentRecordDataFiltered[list(currentRecord)[ITERATOR]] -= 1

    # Check if there is already generated rule
    print("currentRecordData: " + str(currentRecordData))
    print("currentRecordDataFiltered: " + str(currentRecordDataFiltered))
    print("currentRecord: " + str(currentRecord))
    rulesAttributes = []
    ruleWasNotGenerated = True
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
            ruleWasNotGenerated = False
            print(list(currentRecordData)[rule] + " - rule")
        else:
            rulesAttributes.append({list(currentRecordData)[rule]: generatedRule})
            print(list(currentRecordData)[rule] + " - not rule :( - " + str(generatedRule))

    print("rulesAttributes: " + str(rulesAttributes))
    maxValues = getXMaxValues(rulesAttributes, ITERATOR)
    # Generate complicated rule
    if ruleWasNotGenerated:
        GENERATED_RULES = generateNewRule(GENERATED_RULES, currentRecord, maxValues, rulesAttributes, ITERATOR)
        GENERATED_RULES = GENERATED_RULES[0]
        ITERATOR = GENERATED_RULES[1]
    rulesAttributes = []
    # Recount my calcs, because it looks like something went wrong
    print('#####################')


GENERATED_RULES = sorted(GENERATED_RULES, key=lambda ruleSort: ruleSort['index'])


for item in GENERATED_RULES:
    print('{index} - {rule}'.format(index=item['index'], rule=item['rule']))
