import csv
import json
import re


def cleanhtml(raw_html: str) -> str:
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', raw_html)
    return cleantext


def count_comma(word):
    if word.count(",") >= 3:
        return True
    else:
        return False


def clean_dictionaries(csvfile):
    updated_dicts = []
    reader = csv.DictReader(csvfile)
    for row in reader:
        new_item = {}
        for key, val in row.items():
            if val != '':
                new_item[key] = cleanhtml(val)
        updated_dicts.append(new_item)
    return updated_dicts


def nested_dicts(parents, childs):
    nested = []
    for parent in parents:
        try:
            if count_comma(parent['Body (HTML)']):
                parent["Sudėtinis"] = True
        except Exception as e:
            pass

        children_to_append = []
        for child in childs:
            if parent['Handle'] == child['Handle']:
                children_to_append.append(child)
        parent['Children'] = children_to_append
        nested.append(parent)
    return nested


with open("products_export_1.csv", encoding='utf-8', newline='') as csvfile:
    parents, childs = [], []
    for row in clean_dictionaries(csvfile):
        if "Title" in row.keys():
            parents.append(row)
        else:
            childs.append(row)

    with open('data.json', 'w', encoding='utf-8') as json_file:
        json.dump(nested_dicts(parents, childs), json_file, indent=4, ensure_ascii=False)
