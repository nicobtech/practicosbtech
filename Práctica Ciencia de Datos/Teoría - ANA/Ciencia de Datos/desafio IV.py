import pandas as pd
df = pd.read_csv('/Users/frana/Downloads/personas_2011.csv',sep= ";")
print(df)

print(df['seniority_level'])
print(df["seniority_level"].count())
print(df.groupby("seniority_level").count())
print(df.groupby("seniority_level")[["persona_id"]].count())



