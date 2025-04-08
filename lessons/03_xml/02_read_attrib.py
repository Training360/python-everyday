import xml.etree.ElementTree as ET

def read_xml_file(file):
    try:
        tree = ET.parse(file)
        root = tree.getroot()
        employees = []

        for employee in root.findall('.//employee'):
            emp_data = {}
            
            # Attribútumok kezelése
            if 'id' in employee.attrib:
                emp_data['id'] = employee.attrib['id']
            
            # Gyerekelemek kezelése
            for child in employee:
                emp_data[child.tag] = child.text
                
            employees.append(emp_data)
        
        return employees
            
    except ET.ParseError as e:
        print(f"Error parsing XML: {e}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    employees = read_xml_file('./lessons//files/employees_id_attrib.xml')
    print(employees)