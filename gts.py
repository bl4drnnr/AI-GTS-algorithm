import json


# def G(Ep, Eb, E):
#     return (Ep + Eb) / E
#
#
# def A(Ep, Eb):
#     return Ep / (Ep + Eb)

def getRule(ruleName, ruleValue):
    return {
        'wiek': {
            "0": "Wiek = Młody",
            "1": "Wiek = Starczy",
            "2": "Wiek = Prestarczy"
        }.get(ruleValue),
        'wada': {
            "0": "Wada = Krotkowidz",
            "1": "Wada = Dalekowidz"
        }.get(ruleValue),
        'ast': {
            "0": "Astygmatyzm = Nie",
            "1": "Astygmatyzm = Tak"
        }.get(ruleValue),
        'lz': {
            "0": "Lzawienie = Normalne",
            "1": "Lzawienie = Zmniejszone"
        }.get(ruleValue),
        'socz': {
            "0": "Soczewki = Brak",
            "1": "Soczewki = Miekkie",
            "2": "Soczewki = Twarde"
        }.get(ruleValue)
    }.get(ruleName)


def H(z, x, y):
    if x == z:
        return format(z / y + (x / z) ** 0.5, ".2f") + " - rule attribute"
    return format(z / y + (x / z) ** 0.5, ".2f")


def extractData(dataToExtract):
    extracteddata = {
        "wiek": {
            "0": 0,
            "1": 0,
            "2": 0
        },
        "wada": {
            "0": 0,
            "1": 0
        },
        "ast": {
            "0": 0,
            "1": 0
        },
        "lz": {
            "0": 0,
            "1": 0
        }
    }
    for item in dataToExtract:
        for attr, value in item.items():
            if attr != 'socz':
                extracteddata[attr][str(value)] += 1

    return extracteddata


f = open('input.json')
data = json.load(f)

createdRules = []
attrsValues = []
inputDataLen = len(data['inputdata'])
firstRecord = data['inputdata'][0]

for iterate in range(4):
    totalQuantityOfAttr = 1
    totalQuantityOfMismatchAttr = 1
    for i in data['inputdata'][1:]:

        if i[list(firstRecord)[iterate]] == firstRecord[list(firstRecord)[iterate]]:
            totalQuantityOfAttr += 1

        if i[list(firstRecord)[iterate]] == firstRecord[list(firstRecord)[iterate]] \
                and i['socz'] == firstRecord['socz']:
            totalQuantityOfMismatchAttr += 1

    attrsValues.append({list(firstRecord)[iterate]: H(totalQuantityOfAttr, totalQuantityOfMismatchAttr, inputDataLen)})

for rule in attrsValues:
    for k, v in rule.items():
        if "rule" in v:
            createdRules.append("IF {rule} THEN {res}"
                                .format(rule=getRule(k, str(firstRecord[k])), res=getRule('socz', str(firstRecord['socz']))))

print(createdRules)
