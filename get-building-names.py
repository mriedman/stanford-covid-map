import requests
import xml.etree.ElementTree as ET
from kml_parse import getinfo
import json

'''txt = requests.get('https://campus-map.stanford.edu/bldg_info_modal.cfm?bldg_id=05-200A').text
txt = requests.get('https://campus-map.stanford.edu/this_bldg.cfm?bldg_id=05-200A&lat=&lng=').text
root = ET.fromstring(txt)

print(txt)
print(root[0][0].text)
print(root[0][1].text)
for child in root:
    print(child.tag)'''

names = json.load(open('names.json'))

for j in getinfo('stanford-quad-id'):
    id = j.split('<')[0]
    if id not in names:
        txt = requests.get(f'https://campus-map.stanford.edu/this_bldg.cfm?bldg_id={id}&lat=&lng=').text
        root = ET.fromstring(txt)

        print(id)
        print(root[0][0].text)
        names[id] = root[0][0].text

print(names)
with open('names.json', 'w') as f:
    json.dump(names, f)
