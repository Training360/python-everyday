import xml.etree.ElementTree as ET

# új xml dokumentum létrehozása
root = ET.Element('root')
doc = ET.SubElement(root, 'doc')

# elemek hozzáadása
ET.SubElement(doc, 'field1', {'name': 'blah'}).text = 'some value1'
ET.SubElement(doc, 'field2', {'name': 'blah'}).text = 'some value2'

# xml fájlba írás
tree = ET.ElementTree(root)
tree.write('example.xml')
