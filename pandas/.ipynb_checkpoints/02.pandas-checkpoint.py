import pandas as pd

people = {
    'first': ['John', 'Jane', 'Jeremayah'],
    'last': ['Doe', 'Doetoo', 'Macniel'],
    'email': ['johndoe@gmail.com', 'janedoetoo@gmail.com', 'jm@gmail.com']
}

df = pd.DataFrame(people)  # index, rows and columns
print(df)
print(df['email'])        # get by column name, use this primary
print(df.email)           # get by column name
# Series = list of data, one dimenzional array, rows of data, one column
print(type(df['email']))
print(df[['last', 'email']])  # DataFrame not Series

print(df.columns)
print(df.iloc[0])             # the first row
print(type(df.iloc[0]))       # series
print(df.iloc[[0, 1]])        # the first two rows
print(df.iloc[[0, 1], 2])     # the first two rows, only the first two
# iloc search by integer location
# loc search by label
print(df.loc[0])
