import json

def fetch_items(file):
    json_file = open(
        file=file,
        mode='r',
        encoding='utf-8'
    )
    return json.load(json_file)


def salary_statistics(data):
    try:
       
        stat = {
            "count": 0,
            "min": None,
            "max": None,
            "sum": None,
            "avg": None,
        }

        salaries = []
        for employee in data:
            if "yearly_salary" in employee and employee["yearly_salary"] is not None:
                salaries.append(employee["yearly_salary"])
            
        if len(salaries) > 0:
            stat["count"] = len(salaries)
            stat["min"] = min(salaries)
            stat["max"] = max(salaries)
            stat["sum"] = sum(salaries)
            stat["avg"] = sum(salaries) / len(salaries)
        
        return stat
        
    except Exception as e:
        return {"error": f"Failed to calculate statistics: {str(e)}"}
    

if __name__ == "__main__":
    data = fetch_items('./lessons//files/employees.json')
    stat = salary_statistics(data)
    print(stat)