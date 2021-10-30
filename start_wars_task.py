"""
Client request: convert their JSON to CSV.
Client said nothing else and sales are not in the mood to ask questions,
so do it the best way you imagine, so it would be easy to work with that
CSV for who ever will receive it in the client side.
"""


import requests

r = requests.get('https://swapi.dev/api/people')

print(r.json())
