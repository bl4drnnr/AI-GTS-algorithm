from common import getRule, getXMaxValues, generateNewRule, H
from parser import parseInputData, getAllPossibleAttributes, getKeyAttribute, getDecisionAttributes
DATA = parseInputData()
KEY_ATTRIBUTE = getKeyAttribute()
ALL_POSSIBLE_ATTRIBUTES = getAllPossibleAttributes()
RULE_ITERATOR = 2
INPUT_DATA_LENGTH = len(DATA)
GENERATED_RULES = []

for x in range(INPUT_DATA_LENGTH):
    currentRecord = DATA[x]
    currentRecordData = getDecisionAttributes()
    currentRecordDataFiltered = getDecisionAttributes()

    # Collecting information for one current record
    for record in DATA:
        for RULE_ITERATOR in range(len(list(getDecisionAttributes()))):
            if record[list(currentRecord)[RULE_ITERATOR]] == currentRecord[list(currentRecord)[RULE_ITERATOR]]:
                currentRecordData[list(currentRecord)[RULE_ITERATOR]] += 1
                currentRecordDataFiltered[list(currentRecord)[RULE_ITERATOR]] += 1

    # Filter collected data to count values of G, A and H
    for record in DATA:
        if record[KEY_ATTRIBUTE] == currentRecord[KEY_ATTRIBUTE]:
            for RULE_ITERATOR in range(len(list(getDecisionAttributes()))):
                if currentRecord[list(currentRecord)[RULE_ITERATOR]] == record[list(currentRecord)[RULE_ITERATOR]]:
                    currentRecordDataFiltered[list(currentRecord)[RULE_ITERATOR]] -= 1

    # Check if there is already generated rule
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
        else:
            rulesAttributes.append({list(currentRecordData)[rule]: generatedRule})

    # Generate complicated rule
    maxValues = getXMaxValues(rulesAttributes, RULE_ITERATOR)
    if ruleWasNotGenerated:
        generatedRulesRes = generateNewRule(GENERATED_RULES, currentRecord, maxValues, rulesAttributes, RULE_ITERATOR)
        GENERATED_RULES = generatedRulesRes[0]
        RULE_ITERATOR = generatedRulesRes[1]
    rulesAttributes = []

# Sort rules by index
GENERATED_RULES = sorted(GENERATED_RULES, key=lambda ruleSort: ruleSort['index'])

# Print all rules
for item in GENERATED_RULES:
    print('{index} - {rule}'.format(index=item['index'] + 1, rule=item['rule']))
