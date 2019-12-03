import requests, json

url = "https://maps.googleapis.com/maps/api/directions/json?origin=Central+Park&destination=Times+Square&sensor=false&mode=walking"
G_KEY = "<get_your_own>"

data = requests.get(f'{url}&key={G_KEY}')
binary = data.content
output = json.loads(str(binary, 'utf-8'))
print(output['status'])

for route in output['routes']:
    for leg in route['legs']:
        for step in leg['steps']:
            print(step['html_instructions'])

for route in output['routes']:
    for leg in route['legs']:
        print(leg['start_address'])
        print(leg['end_address'])
