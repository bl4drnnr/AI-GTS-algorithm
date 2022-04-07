def getRule(ruleName, ruleValue):
    return {
        'Wiek': {
            0: "Wiek = Młody",
            1: "Wiek = Starczy",
            2: "Wiek = Prestarczy"
        }.get(ruleValue),
        'Wada_wzroku': {
            0: "Wada = Krotkowidz",
            1: "Wada = Dalekowidz"
        }.get(ruleValue),
        'Astygmatyzm': {
            0: "Astygmatyzm = Nie",
            1: "Astygmatyzm = Tak"
        }.get(ruleValue),
        'Lzawienie': {
            0: "Lzawienie = Normalne",
            1: "Lzawienie = Zmniejszone"
        }.get(ruleValue),
        'SOCZEWKI': {
            0: "Soczewki = Brak",
            1: "Soczewki = Miekkie",
            2: "Soczewki = Twarde"
        }.get(ruleValue)
    }.get(ruleName)


def getTwoMaxValue(obj):
    return sorted(obj, key=lambda dct: list(dct.values())[0])[-2:]


def H(Epb, Ep, E):
    if Ep / Epb == 1:
        return "rule"
    return format((Epb / E) + (Ep / Epb) ** 0.5, ".3f")
