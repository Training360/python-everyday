# Feladatok

1. Írj egy függvény, amely bekéri a felhasználó nevét, majd kiírja ezt az adatot egy szöveges fájlba! A fájlnevet
   paraméterként kapja a függvény.
2. Hozz létre egy szöveges fájlt, amelyben egész számok sorozatát tároljuk, vesszővel elválasztva! Írj egy Python
   függvényt, amely beolvassa a fájlt, majd visszatér az összes szám összegével! A fájlnevet
   paraméterként kapja a függvény.
3. Adott egy szöveges fájl (`primarchs.txt`), amelyben soronként nevek szerepelnek. Írj egy Python függvényt, amely
   beolvassa a fájlt, majd visszatér a nevek listájával, abc-sorrendben rendezve! A fájlnevet
   paraméterként kapja a függvény.
4. Hozz létre egy szöveges fájlt tetszőleges tartalommal! Írj egy függvényt, amely statisztikát készít a tartalomról egy
   dictionary-be, és visszaadja azt. A kulcsok az alábbiak:
    - line_count: sorok száma
    - words_count: szavak száma
    - characters_length: a karakterek száma (minden karakter, whitespace karakterek is)
      A fájlnevet paraméterként kapja a függvény.

   ```python
   
   def file_stats(filename):
       stats = {
           'line_count': 0,
           'words_count': 0,
           'characters_length': 0
       }
   
       with open(filename, 'r') as f:
           for line in f:
               stats['line_count'] += 1
               stats['words_count'] += len(line.split())
               stats['characters_length'] += len(line)
   
       return stats
      ```

7 Írj egy Python függvényt, amely a következő feladatokat végzi el:

Beolvassa egy könyvtárban található összes fájl nevét és méretét.
Minden fájlnévre, amely végződik ".txt"-vel, létrehoz egy kulcsot a dictionary-ben, és hozzárendel egy értéket, amely a
fájl mérete.
A függvény visszatérési értéke a dictionary a dictionary.
Feladat megoldása:

```py
import os


def count_txt_files(path):
    files_dict = {}
    for file in os.listdir(path):
        if file.endswith(".txt"):
            file_path = os.path.join(path, file)
            files_dict[file] = os.path.getsize(file_path)
    return files_dict
```

5. Adott egy JSON fájl (`users.json`), amelyben emberek adatai találhatók (vezetéknév, keresztnév, életkoruk). Írj egy
   függvényt, ami beolvassa a fájlt, és visszaadja az átlagéletkort!

   ```python
   import json
   
   
   def calculate_avg_age(file_name):
       with open(file_name, 'r') as f:
           users = json.load(f)
       ages = [user['age'] for user in users]
       avg_age = sum(ages) / len(ages)
       return avg_age
   ```

6 Adott egy CSV fájl, amelyben országok nevei és GDP-jük találhatók. Olvassuk be a fájlt, és írjunk egy függvényt,
amely visszaadja az országok átlagos GDP-jét!
Könyvtárak számontartása

8. Adott egy XML fájl, amelyben filmek adatai találhatók (title, studio, producer, yart). Olvassuk be a fájlt, és írjuk
   ki az összes film címét és megjelenési évének számát egy új XML fájlba, amely csak ezeket az adatokat tartalmazza!

```python
import json


def calculate_avg_age(file_name):
    with open(file_name, 'r') as f:
        users = json.load(f)
    ages = [user['age'] for user in users]
    avg_age = sum(ages) / len(ages)
    return avg_age
```

9 2 json összefűzése, duplikátumok eltávolítása

```python
import json


def merge_and_remove_duplicates(json_file1, json_file2, output_file):
    with open(json_file1, 'r') as f1:
        data1 = json.load(f1)
    with open(json_file2, 'r') as f2:
        data2 = json.load(f2)
    merged_data = data1 + data2

    unique_data = []
    for item in merged_data:
        if json.dumps(item) not in unique_data:
            unique_data.append(json.dumps(item))

    unique_data = [json.loads(item) for item in unique_data]

    # 5. Írjuk ki az új objektumot egy JSON fájlba
    with open(output_file, 'w') as f:
        json.dump(unique_data, f)


# Teszteljük a függvényt:
merge_and_remove_duplicates('data1.json', 'data2.json', 'merged_data.json')
```

Adott egy csv fájl felhasználók nevével és email címével. Konvertáld át json és cml formátumra is..

```python
import csv
import json
import xml.etree.ElementTree as ET

# Olvassuk be a CSV fájlt és tároljuk el egy listában
with open('felhasznalok.csv', newline='') as f:
    reader = csv.DictReader(f)
    users = [row for row in reader]

# Konvertáljuk JSON formátumra
with open('felhasznalok.json', 'w') as f:
    json.dump(users, f, indent=4)

# Konvertáljuk XML formátumra
root = ET.Element('users')
for user in users:
    node = ET.SubElement(root, 'user')
    ET.SubElement(node, 'name').text = user['name']
    ET.SubElement(node, 'email').text = user['email']
tree = ET.ElementTree(root)
tree.write('felhasznalok.xml', encoding='UTF-8', xml_declaration=True)
```
