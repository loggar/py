import pandas as pd

df = pd.read_csv('gdp.csv', index_col=0)

for val in df:
    print(val)

for label, row in df.iterrows():
    print(label)
    print(row)

for label, row in df.iterrows():
    print(label + " : " + row["Capital"])

for label, row in df.iterrows():
    df.loc[label, 'gdp_per_cap'] = row['GDP ($US Trillion)'] / \
        row['Population '] * 1000000000000
print(df)
