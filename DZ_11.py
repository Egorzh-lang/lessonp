import pandas as pd

df=pd.read_csv("./", sep=",")
df=df.dropna()
df=df.groupby("HAD_CPOX")["SEX"].mean()
print(df)
