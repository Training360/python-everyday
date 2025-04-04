from lxml import etree
import os

def append_to_xml(xml_file, new_data, item_name):

    if not os.path.exists(xml_file):
        raise FileNotFoundError(f"XML file '{xml_file}' not found")
    
    parser = etree.XMLParser(remove_blank_text=True)
    tree = etree.parse(xml_file, parser)
    root = tree.getroot()
    
    if isinstance(new_data, dict):
        new_data = [new_data]
    
    for item in new_data:
        employee_elem = etree.SubElement(root, item_name)
        
        for key, value in item.items():
            child = etree.SubElement(employee_elem, key)
            child.text = str(value)
    
    tree.write(xml_file, pretty_print=True, encoding="utf-8", xml_declaration=True)

# Example usage
new_employee = {
    "id": 1003,
    "first_name": "Robert",
    "last_name": "Johnson",
    "email": "robert.johnson@example.com",
    "gender": "Male",
    "salary": 78000,
    "years_of_experience": 3
}

# Append to existing XML file
append_to_xml("./lessons/xml/files/new_employees.xml", new_employee, "employee")