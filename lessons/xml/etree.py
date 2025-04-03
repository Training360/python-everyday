import xml.etree.ElementTree as ET
from os import path

tree = ET.parse('books.xml')
root = tree.getroot()

print(root[0].tag)
print(root[0].attrib)

print(root[0][0].tag)
print(root[0][0].attrib)
print(root[0][0].text)

# kilistázzuk az összes gyermek elemet a fájlban az attributumokkal együtt


for child in root:
    print(child.tag, child.attrib)

# adott elem keresése
for child in root.iter("title"):
    print(child.text, child.attrib)
