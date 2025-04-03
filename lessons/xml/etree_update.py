import xml.etree.ElementTree as ET

# xml fájl beolvasása
tree = ET.parse("example.xml")
root = tree.getroot()

# módosítjuk a child1 elemet
for child in root.iter("field1"):
    child.text = "Modified text of child 1"
    child.set("attribute", "new attribute value")

for child in root.iter("field2"):
    root.remove(child)
# mentjük az xml fájlt
tree.write("modified_example.xml")
