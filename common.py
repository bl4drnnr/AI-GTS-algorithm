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


def H(Epb, Ep, E):
    if Ep / Epb == 1:
        return "rule attribute"
    return format((Epb / E) + (Ep / Epb) ** 0.5, ".2f")


# def G(Ep, Eb, E):
#     return (Ep + Eb) / E
#
#
# def A(Ep, Eb):
#     return Ep / (Ep + Eb)

