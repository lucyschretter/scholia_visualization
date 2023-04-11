from pandas import read_csv
import pandas as pd

df = read_csv('query.csv')

print(df.columns)

# The scope of these changes made to
# pandas settings are local to with statement.
with pd.option_context('display.max_rows', None,
                       'display.max_columns', None,
                       ):
    print(df)
