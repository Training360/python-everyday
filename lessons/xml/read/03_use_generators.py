import xml.etree.ElementTree as ET

def read_xml_file_generator(file):
    """Generator function that yields employee records one at a time"""
    try:
        tree = ET.parse(file)
        root = tree.getroot()

        for employee in root.findall('.//employee'):
            emp_data = {}
            
            if 'id' in employee.attrib:
                emp_data['id'] = employee.attrib['id']
            
            for child in employee:
                emp_data[child.tag] = child.text
                
            yield emp_data
            
    except ET.ParseError as e:
        print(f"Error parsing XML: {e}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":        
    employees = list(read_xml_file_generator('./lessons/xml/files/employees.xml'))
    print(employees)