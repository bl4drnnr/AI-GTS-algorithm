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
    maxValues = getXMaxValues(rulesAttributes, ITERATOR)
    # Generate complicated rule
    if ruleWasNotGenerated:
        test = generateNewRule(GENERATED_RULES, currentRecord, maxValues, rulesAttributes, ITERATOR)
        GENERATED_RULES = test[0]
        # ITERATOR = 2
        ITERATOR = test[1]
    rulesAttributes = []
    # Recount my calcs, because it looks like something went wrong
    print('#####################')


GENERATED_RULES = sorted(GENERATED_RULES, key=lambda ruleSort: ruleSort['index'])


for item in GENERATED_RULES:
    print('{index} - {rule}'.format(index=item['index'] + 1, rule=item['rule']))

# 1 - IF Lzawienie = normalne AND Astygmatyzm = nie THEN SOCZEWKI = miekkie
# 2 - IF Wiek = mlody AND Lzawienie = normalne AND Astygmatyzm = tak THEN SOCZEWKI = twarde
# 3 - IF Lzawienie = zmniejszone THEN SOCZEWKI = brak
# 4 - IF Lzawienie = zmniejszone THEN SOCZEWKI = brak
# 5 - IF Lzawienie = zmniejszone THEN SOCZEWKI = brak
# 6 - IF Lzawienie = normalne AND Astygmatyzm = nie THEN SOCZEWKI = miekkie
# 7 - IF Wiek = mlody AND Lzawienie = normalne AND Astygmatyzm = tak THEN SOCZEWKI = twarde
# 8 - IF Lzawienie = zmniejszone THEN SOCZEWKI = brak
# 9 - IF Lzawienie = zmniejszone THEN SOCZEWKI = brak
# 10 - IF Lzawienie = zmniejszone THEN SOCZEWKI = brak
# 11 - IF Lzawienie = zmniejszone THEN SOCZEWKI = brak
# 12 - IF Lzawienie = zmniejszone THEN SOCZEWKI = brak
# 13 - IF Wada_wzroku = krotkowidz AND Lzawienie = normalne AND Astygmatyzm = tak THEN SOCZEWKI = twarde
# 14 - IF Lzawienie = normalne AND Astygmatyzm = nie THEN SOCZEWKI = miekkie
# 15 - IF Wiek = starczy AND Astygmatyzm = tak AND Wada_wzroku = dalekowidz THEN SOCZEWKI = brak
# 16 - IF Lzawienie = zmniejszone THEN SOCZEWKI = brak
# 17 - IF Lzawienie = zmniejszone THEN SOCZEWKI = brak
# 18 - IF Lzawienie = zmniejszone THEN SOCZEWKI = brak
# 19 - IF Lzawienie = zmniejszone THEN SOCZEWKI = brak
# 20 - IF Lzawienie = normalne AND Astygmatyzm = nie THEN SOCZEWKI = miekkie
# 21 - IF Lzawienie = normalne AND Astygmatyzm = nie THEN SOCZEWKI = miekkie
# 22 - IF Wiek = prestarczy AND Astygmatyzm = tak AND Wada_wzroku = dalekowidz THEN SOCZEWKI = brak
