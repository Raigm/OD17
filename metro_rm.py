import requests
from lxml import etree
import xml.etree.ElementTree as ET

# stations = requests.get("https://data.tfl.gov.uk/tfl/syndication/feeds/stations-facilities.xml?app_id=3c300fe8&app_key=4c8ac4128a27f1ba7b3e8bce8e099cc4")
step_free = requests.get("https://tfl.gov.uk/tfl/syndication/feeds/step-free-tube-guide.xml")
# stations.write("stations.xml")
stations = requests.get("https://data.tfl.gov.uk/tfl/syndication/feeds/stations-facilities.xml?app_id=3c300fe8&app_key=4c8ac4128a27f1ba7b3e8bce8e099cc4")
req = requests.request("GET","https://data.tfl.gov.uk/tfl/syndication/feeds/stations-facilities.xml?app_id=3c300fe8&app_key=4c8ac4128a27f1ba7b3e8bce8e099cc4")
print(req)

# print(stations.content)
# print(stations.text)
#
tree = etree.parse(stations.text)
root=tree.getroot()
# print(tree)
#
# doc=etree.parse('stations.xml')#Aquí estoy cargando el xml, que habia exportado
# for elem in root.findall('//openingHours'):
#    parent = elem.getparent()
#    parent.remove(elem)
#    print(etree.tostring(root))
#
# root = doc.getroot()
# print(root.find("stations/station/openingHours"))
# print(root.findall("stations/station/openingHours"))
# print(root.findtext("stations/station/openingHours"))