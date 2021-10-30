import requests

r = requests.get('https://swapi.dev/api/people')

print(r.json())
