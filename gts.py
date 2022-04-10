from common import getRule, getXMaxValues, generateNewRule, H
from parser import parseInputData, getAllPossibleAttributes, getKeyAttribute, getDecisionAttributes
DATA = parseInputData()
KEY_ATTRIBUTE = getKeyAttribute()
ALL_POSSIBLE_ATTRIBUTES = getAllPossibleAttributes()
ITERATOR = 1
INPUT_DATA_LENGTH = len(DATA)
GENERATED_RULES = []

for x in range(INPUT_DATA_LENGTH):
    currentRecord = DATA[x]
    currentRecordData = getDecisionAttributes()
    currentRecordDataFiltered = getDecisionAttributes()

    # Collecting information for one current record
    for record in DATA:
        for attribute in range(len(list(getDecisionAttributes()))):
            if record[list(currentRecord)[attribute]] == currentRecord[list(currentRecord)[attribute]]:
                currentRecordData[list(currentRecord)[attribute]] += 1
                currentRecordDataFiltered[list(currentRecord)[attribute]] += 1

    # Filter collected data to count values of G, A and H
    for record in DATA:
        if record[KEY_ATTRIBUTE] == currentRecord[KEY_ATTRIBUTE]:
            for attribute in range(len(list(getDecisionAttributes()))):
                if currentRecord[list(currentRecord)[attribute]] == record[list(currentRecord)[attribute]]:
                    currentRecordDataFiltered[list(currentRecord)[attribute]] -= 1

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
            pushSimpleRule = True
            for generated_rule in GENERATED_RULES:
                if generated_rule['index'] == x:
                    pushSimpleRule = False
                    print(str(generated_rule) + " " + str(x))
            if pushSimpleRule:
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
    # Generate complicated rule
    if ruleWasNotGenerated:
        maxValues = getXMaxValues(rulesAttributes, ITERATOR)
        test = generateNewRule(GENERATED_RULES, currentRecord, maxValues, rulesAttributes, ITERATOR)
        GENERATED_RULES = test[0]
        ITERATOR = test[1]
    rulesAttributes = []
    # Recount my calcs, because it looks like something went wrong
    print('#####################')


GENERATED_RULES = sorted(GENERATED_RULES, key=lambda ruleSort: ruleSort['index'])


for item in GENERATED_RULES:
    print('{index} - {rule}'.format(index=item['index'] + 1, rule=item['rule']))
