import pandas as pd
df = pd.read_csv('/Users/frana/Downloads/personas_2011.csv',sep= ";")
print(df)

print(df.head())
print(df.info())
print(df.describe())
print(df[' persona_id'])
print(df.loc[2, 'persona_id'])
print(df[' persona_id'].tolist())
print(df["seniority_level"].count())
print(df.groupby("seniority_level").count())
print(df.groupby("seniority_level")[["persona_id"]].count())

print(df['edad'] * 2)
print(df['edad'] + 2)
print(df['edad'] > 2)

print(df[df['edad'] > 35 ])

df3 = pd.merge(df, df_cat, on='categoria_conicet_id')
print(df3)
