import csv
import numpy as np
from collections import Counter
from matplotlib import pyplot as plt
from os import path

plt.style.use('seaborn-v0_8-bright')

with open(path.join(path.dirname(__file__), 'survey_light.csv')) as csv_file:
    csv_reader = csv.DictReader(csv_file)
    language_counter = Counter()
    for row in csv_reader:
        language_counter.update(row['LanguageWorkedWith'].split(';'))

# print(language_counter)
# print(language_counter.most_common(10))

languages = []
popularity = []
for item in language_counter.most_common(15):
    languages.append(item[0])
    popularity.append(item[1])

print(languages)
print(popularity)

languages.reverse()
popularity.reverse()
plt.barh(languages, popularity)

#     row = next(csv_reader)
#     print(row['LanguageWorkedWith'].split(';'))

plt.title("Most popular programming languages")
plt.ylabel('PRogramming languages')
plt.xlabel('Number of people who use')

plt.tight_layout()

plt.show()
