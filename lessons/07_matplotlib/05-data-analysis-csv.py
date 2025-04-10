import csv
import numpy as np
import pandas as pd
from collections import Counter
from matplotlib import pyplot as plt

plt.style.use('seaborn-v0_8-bright')

data = pd.read_csv('./lessons/files//survey_light.csv')
ids = data['Respondent']
lang_responses = data['LanguageWorkedWith']
language_counter = Counter()

for response in lang_responses:
    language_counter.update(str(response).split(';'))

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
