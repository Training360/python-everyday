import pandas as pd

df = pd.read_csv('pandas/stackowerflow/survey_results_public.csv')
schema_df = pd.read_csv('pandas/stackowerflow/survey_results_schema.csv')
# print(df)
print(df.shape)
print(df.info())    # types

pd.set_option('display.max_columns', 85)
pd.set_option('display.max_rows', 85)
# print(df)

print(df.head(3))
print(schema_df)
