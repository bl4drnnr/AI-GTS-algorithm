import json
f = open('input.json')
data = json.load(f)

for i in data['inputdata']:
    print(i)
