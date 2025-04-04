from lxml import etree

def transform_xml(input_file, output_file):
    # Parse the XML file
    tree = etree.parse(input_file)
    root = tree.getroot()
    
    # Process each employee element
    for employee in root.findall('employee'):
        # Skip empty employee elements
        if len(employee) == 0:
            continue
            
        # Get the relevant elements
        first_name_elem = employee.find('first_name')
        last_name_elem = employee.find('last_name')
        yearly_salary_elem = employee.find('yearly_salary')
        years_of_experience_elem = employee.find('years_of_experience')
        
        # Transform name - create a name element containing first_name and last_name
        if first_name_elem is not None and last_name_elem is not None:
            # Először tároljuk el az indexet!
            first_name_index = list(employee).index(first_name_elem)
            
            # Create a new name parent element
            name_elem = etree.Element('name')
            
            # Move first_name and last_name inside the name element
            name_elem.append(first_name_elem)
            name_elem.append(last_name_elem)
            
            # Insert the name element at the position where first_name was
            employee.insert(first_name_index, name_elem)
        
        # Transform salary - replace yearly_salary with salary having experience attribute
        if yearly_salary_elem is not None and years_of_experience_elem is not None:
            # Create new salary element with yearly_salary value
            salary_elem = etree.Element('salary')
            salary_elem.text = yearly_salary_elem.text
            
            # Add experience attribute with years_of_experience value
            salary_elem.set('experience', years_of_experience_elem.text)
            
            # Replace yearly_salary with new salary element
            employee.replace(yearly_salary_elem, salary_elem)
            
            # Remove years_of_experience element
            employee.remove(years_of_experience_elem)
    
    # Write the transformed XML to the output file
    tree.write(output_file, pretty_print=True, encoding='utf-8', xml_declaration=True)
    print(f"Transformed XML written to {output_file}")

if __name__ == "__main__":
    input_file = "./lessons/xml/files/employees.xml"
    output_file = "./lessons/xml/files/employees_transformed.xml"
    transform_xml(input_file, output_file)