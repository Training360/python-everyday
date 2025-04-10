import xml.etree.ElementTree as ET
import json


def process_attributes(element, result):
    """Add all attributes from the element to the result dictionary"""
    result.update(element.attrib)
    return result


def process_text(element, result):
    text = element.text.strip() if element.text else ""
    if text and not result:
        return text
    elif text:
        result["#text"] = text
    return result


def process_children(element, result):
    """Process all child elements recursively"""
    for child in element:
        child_data = xml_to_dict(child)

        if child.tag in result:
            # Handle duplicate tags by converting to list
            if isinstance(result[child.tag], list):
                result[child.tag].append(child_data)
            else:
                result[child.tag] = [result[child.tag], child_data]
        else:
            result[child.tag] = child_data

    return result


def xml_to_dict(element):
    """Convert XML element to dictionary recursively"""
    result = {}
    result = process_attributes(element, result)
    result = process_children(element, result)
    result = process_text(element, result)
    return result


def read_complex_xml_generator(file):
    try:
        tree = ET.parse(file)
        root = tree.getroot()

        for employee in root.findall(".//employee"):
            emp_data = xml_to_dict(employee)
            yield emp_data

    except ET.ParseError as e:
        print(f"Error parsing XML: {e}")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    employees = list(read_complex_xml_generator("./files/employees_complex.xml"))
    print(json.dumps(employees, indent=2))
