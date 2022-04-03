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

import json
f = open('input.json')
data = json.load(f)

for i in data['inputdata']:
    print(i)
