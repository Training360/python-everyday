from lxml import etree

def read_xml_file(file_path):
    try:
        return etree.parse(file_path)
    except Exception as e:
        print(f"Hiba: {e}")
        return None

def salary_stat(doc):
    salaries = doc.xpath('//salary')
    values = []
    stat = {"count": 0, "min": None, "max": None, "sum": None, "avg": None,  }
    
    for salary in salaries:
        if salary.text:
            values.append(float(salary.text))
    
    if values:
            stat["count"] = len(values)
            stat["min"] = min(values)
            stat["max"] = max(values)
            stat["sum"] = sum(values)
            stat["avg"] = stat["sum"] /  stat["count"]
        
    return stat 


if __name__ == "__main__":
    dom_doc = read_xml_file("./lessons/xml/files/employees_complex.xml")
    stat = salary_stat(dom_doc)
    print(stat)