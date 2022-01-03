import requests
import xml.etree.ElementTree as ET

txt = requests.get('https://campus-map.stanford.edu/bldg_info_modal.cfm?bldg_id=05-200A').text
txt = requests.get('https://campus-map.stanford.edu/this_bldg.cfm?bldg_id=05-200A&lat=&lng=').text
root = ET.fromstring(txt)

print(txt)
print(root[0][0].text)
print(root[0][1].text)
for child in root:
    print(child.tag)
