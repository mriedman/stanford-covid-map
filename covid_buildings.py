import csv
import io
from datetime import datetime
import json

places = {}

with open('pos.csv', 'rb') as f:
    s = str(f.read()[::2]).replace('\\t', '\t').replace('\\n', '\n')
    print(s)
    f1 = io.StringIO(s)
    reader = csv.reader(f1, dialect='excel-tab')
    for row in reader:
        if len(row) > 2 and row[0] not in places:
            try:
                places[row[0]] = f"ago-{(datetime.now() - datetime.strptime(row[2], '%m/%d/%Y')).days}"
            except ValueError:
                pass

json.dump(places, open('covid-locs.json','w'))
