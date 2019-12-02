import json


output = json.load(open('cars.json'))
print(output)
print(json.dumps(output, indent=4, sort_keys=True))