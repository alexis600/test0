
from xml.dom.minidom import parse, Node
xmltree = parse("tax.xml")

for nodo in xmltree.getElementsByTagName ("page"):
    #elementsbyname es case sensitive
    for nodo_hijo in nodo.childNodes:
        if nodo_hijo.nodeType == Node.TEXT_NODE:
            print (nodo_hijo.data)


import xml.sax
from xml.etree.ElementTree import parse

xml_doc = parse("tax.xml")
for ele in xml_doc.findall("page"):
    print(ele.text)
    
    

#JSON
import json
with open("note.json") as file:
    data = json.load(file)
print(data)
print(data['clientesB'])
    
