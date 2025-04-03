import xml.etree.ElementTree as ET
import csv
import json
import os

def xml_to_xml(xml_file):
    # Parse XML file
    tree = ET.parse(xml_file)
    root = tree.getroot()
    
    # Extract data
    employees = []
    for employee in root.findall('employee'):
        emp_data = {}
        for child in employee:
            emp_data[child.tag] = child.text
        employees.append(emp_data)
    
    # Create a new XML structure
    output_root = ET.Element("employees")
    for emp in employees:
        # Create employee element
        emp_element = ET.SubElement(output_root, "employee")
        
        # Set id as attribute if it exists
        if 'id' in emp:
            emp_element.set('id', emp['id'])
            # Create child elements for all other fields
            for key, value in emp.items():
                if key != 'id':  # Skip id as it's now an attribute
                    child = ET.SubElement(emp_element, key)
                    child.text = value
        else:
            # If no id exists, create child elements for all fields
            for key, value in emp.items():
                child = ET.SubElement(emp_element, key)
                child.text = value
    
    # Create the output XML file
    output_xml = xml_file.replace('.xml', '_output.xml')
    tree = ET.ElementTree(output_root)
    tree.write(output_xml, encoding='utf-8', xml_declaration=True)
    print(f"XML file created: {output_xml}")

if __name__ == "__main__":
    xml_file = "./lessons/csv/employees.xml"
    xml_to_xml(xml_file)