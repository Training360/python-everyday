from lxml import etree

def list_dict_to_xml(data_list, root_name, item_name, output_file):
    root = etree.Element(root_name)
    
    for item in data_list:
        employee_elem = etree.SubElement(root, item_name)
        
        for key, value in item.items():
            child = etree.SubElement(employee_elem, key)
            child.text = str(value)
    
    tree = etree.ElementTree(root)
    tree.write(output_file, pretty_print=True, encoding="utf-8", xml_declaration=True)

if __name__ == "__main__":
    # Example usage
    employees = [
        {
            "id": 1001,
            "first_name": "John",
            "last_name": "Doe",
            "email": "john.doe@example.com",
            "gender": "Male",
            "salary": 85000,
            "years_of_experience": 5
        },
        {
            "id": 1002,
            "first_name": "Jane",
            "last_name": "Smith",
            "email": "jane.smith@example.com",
            "gender": "Female",
            "salary": 92000,
            "years_of_experience": 7
        }
    ]

    list_dict_to_xml(employees, "employees", "employee", "./lessons/xml/files/new_employees.xml")