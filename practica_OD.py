
import requests
from lxml import etree
import xml.etree.ElementTree as ET

#1. Acceder a la página de datos abiertos de TfL y descargar ambos datasets a través de API.

stations = requests.get("https://data.tfl.gov.uk/tfl/syndication/feeds/stations-facilities.xml?app_id=3c300fe8&app_key=4c8ac4128a27f1ba7b3e8bce8e099cc4")
step_free = requests.get("https://tfl.gov.uk/tfl/syndication/feeds/step-free-tube-guide.xml")

stations.encoding='UTF-8'
with open('StationFacilities.xml', 'w') as f:
    f.write(stations.text)

step_free.encoding='UTF-8'
with open('StepFreeTube.xml', 'w') as f:
    f.write(step_free.text)

#2. Generar un fichero similar a a), denominado StationFacilitiesNOH, donde no se incorpore la información asociada a las etiquetas , ni las propias etiquetas.

doc=etree.parse('StationFacilities.xml')#Importo Station facilities
for elem in doc.xpath('.//openingHours'):
   parent = elem.getparent()
   parent.remove(elem)
   print(etree.tostring(doc))
   doc.write('StationFacilities_NOH.xml')

#3. Generar un fichero similar a b), denominado StepFreeTubeNNone, que no debe incorporar la información asociada a las etiquetas (ni las propias etiquetas) cuando el contenido sea None.

doc2 = etree.parse('StepFreeTube.xml')

for elem in doc2.xpath("//*[text()='None']"):
    parent = elem.getparent()
    parent.remove(elem)
    doc2.write('StepFreeTubeNNone.xml')
