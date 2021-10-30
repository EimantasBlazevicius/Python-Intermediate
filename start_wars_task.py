"""
Client request: convert their JSON to CSV.
Client said nothing else and sales are not in the mood to ask questions,
so do it the best way you imagine, so it would be easy to work with that
CSV for who ever will receive it in the client side.
"""

import requests
import csv
from time import sleep


header = 'Mozilla/5.0 (platform; rv:geckoversion) Gecko/geckotrail Firefox/firefoxversion'
r = requests.get('https://swapi.dev/api/people', headers={'User-Agent': header})


with open("star_wars.csv", "a+", newline='') as file:

    writer = csv.writer(file)
    data = r.json()
    results = data.get('results')
    writer.writerow(results[0].keys())
    while True:
        sleep(0.1)
        data = r.json()
        next_link = data.get('next')
        results = data.get('results')
        for result in results:
            writer.writerow(result.values())

        if next_link is not None:
            r = requests.get(next_link, headers={'User-Agent': header})
        else:
            break
