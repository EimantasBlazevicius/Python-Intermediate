import csv
import json
import re


def cleanhtml(raw_html):
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', raw_html)
    return cleantext


def count_comma(description):
    return True if description.count(",") >= 3 else False


def clean_dictionaries(csvfile):
    reader = csv.DictReader(csvfile)
    for row in reader:
        new_item = {}
        for key, val in row.items():
            if val != '':
                new_item[key] = cleanhtml(val)
        yield new_item


def nested_dicts(parents, childs):
    nested = []
    for parent in parents:
        try:
            if count_comma(parent['Body (HTML)']):
                parent["Sudėtinis"] = True
        except Exception:
            pass
        children_to_append = []
        for child in childs:
            if parent['Handle'] == child['Handle']:
                children_to_append.append(child)
        parent['Children'] = children_to_append
        nested.append(parent)
    return nested


if __name__ == "__main__":
    try:
        with open("products_export_1.csv", encoding='utf-8') as csvfile:
            parents, childs = [], []
            for row in clean_dictionaries(csvfile):
                if "Title" in row.keys():
                    parents.append(row)
                else:
                    childs.append(row)
            with open('data.json', 'w', encoding='utf-8') as json_file:
                json.dump(nested_dicts(parents, childs), json_file, indent=4, ensure_ascii=False)
    except Exception as e:
        with open('logs.txt', 'w') as logs:
            logs.write(e)
