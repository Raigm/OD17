import requests
from lxml import etree
import xml.etree.ElementTree as ET


#1. Acceder a la página de datos abiertos de TfL y descargar ambos datasets a través de API.
stations = requests.get("https://data.tfl.gov.uk/tfl/syndication/feeds/stations-facilities.xml?app_id=3c300fe8&app_key=4c8ac4128a27f1ba7b3e8bce8e099cc4")
step_free = requests.get("https://tfl.gov.uk/tfl/syndication/feeds/step-free-tube-guide.xml")

with open('StationFacilities.xml', 'w') as f:
    f.write(stations.text)

with open('StepFreeTube.xml', 'w') as f:
    f.write(step_free.text)


# tree = etree.parse(stations.text) Posible texto para hacer la integracion directamente
# root=tree.getroot()

#2. Generar un fichero similar a a), denominado StationFacilitiesNOH, donde no se incorpore la información asociada a las etiquetas <openingHours>xxxx</openingHours>, ni las propias etiquetas.
doc=etree.parse('StationFacilities.xml')#Importo Station facilities
for elem in doc.xpath('.//openingHours'):
   parent = elem.getparent()
   parent.remove(elem)
   print(etree.tostring(doc))
   doc.write('StationFacilities_NOH.xml')

#3. Generar un fichero similar a b), denominado StepFreeTubeNNone, que no debe incorporar la información asociada a las etiquetas <AccessibilityType>None</AccessibilityType> (ni las propias etiquetas) cuando el contenido sea None.
doc2 = etree.parse('StepFreeTube.xml')  # Importo Station facilities
for elem in doc2.xpath('.//*[attribute::AccesibilityTpye]'):
    if elem.attrib['AccesibilityType']!='None':
        elem.attrib.pop('AccesibilityType')
    else:
        parent = elem.getparent()
        parent.remove(elem)
    print(etree.tostring(doc2))
    doc2.write('StepFreeTubeNNone.xml')




       # root = doc.getroot()
# print(root.find("stations/station/openingHours"))
# print(root.findall("stations/station/openingHours"))
# print(root.findtext("stations/station/openingHours"))