import json


def G(Ep, Eb, E):
    return (Ep + Eb) / E


def A(Ep, Eb):
    return Ep / (Ep + Eb)


def H(Gvalue, Avalue):
    return Gvalue + Avalue ** 1 / 2


createdRules = []

f = open('input.json')
data = json.load(f)

for i in data['inputdata']:
    print(i)


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