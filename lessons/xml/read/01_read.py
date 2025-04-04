from lxml import etree

def read_xml_file(file):
    try:
        tree = etree.parse(file)
        root = tree.getroot()
        employees = []

        for employee in root.xpath('//employee'):
            emp_data = {}
       
            for child in employee:
                emp_data[child.tag] = child.text
                
            employees.append(emp_data)
        
        return employees
            
    except etree.XMLSyntaxError as e:
        print(f"Error parsing XML: {e}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    employees = read_xml_file('./lessons/xml/files/employees.xml')
    print(employees)