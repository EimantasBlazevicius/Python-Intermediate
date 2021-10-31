import requests
import csv
from time import sleep


header = 'Mozilla/5.0 (platform; rv:geckoversion) Gecko/geckotrail Firefox/firefoxversion'
r = requests.get('https://swapi.dev/api/people', headers={'User-Agent': header})


def convert_to_string(value: list) -> str:
    return '' if len(value) == 0 else '; '.join(value)


with open("star_wars.csv", "w", newline='', encoding='utf-8') as file:
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
            updated_values = [item if type(item) != list else convert_to_string(item) for item in result.values()]
            print(updated_values)
            writer.writerow(updated_values)
            # writer.writerow(result.values())

        if next_link is not None:
            r = requests.get(next_link, headers={'User-Agent': header})
        else:
            break