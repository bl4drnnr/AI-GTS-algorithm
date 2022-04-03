import json


def G(Ep, Eb, E):
    return (Ep + Eb) / E


def A(Ep, Eb):
    return Ep / (Ep + Eb)


def H(Gvalue, Avalue):
    return Gvalue + Avalue ** 1 / 2


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
                # extracteddata[attr][value] += 1

    return extracteddata


f = open('input.json')
data = json.load(f)

createdRules = []
inputDataLen = len(data['inputdata'])
firstRecord = data['inputdata'][0]

print(extractData(data['inputdata']))

# for i in data['inputdata'][1:]:

# WIEK:
#   Mlody - 0
#   starczy - 1
#   prestarczy - 2

# WADA:
#   Krot - 0
#   Dal - 1

# AST:
#   Nie - 0
#   Tak - 1

# LZ:
#   Norm - 0
#   Zmn - 1

# SOCZ:
#   Brak - 0
#   Miekkie - 1
#   Twarde - 2
