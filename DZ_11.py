import pandas as pd

df=pd.read_csv("./NIS-PUF17-DUG", sep=",")
df=df.dropna()
df=df.groupby("HAD_CPOX")["SEX"].mean()
print(df)
