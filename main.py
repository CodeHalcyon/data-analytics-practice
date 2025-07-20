import numpy as np
import pandas as pd

df = pd.read_csv("Titanic-Dataset.csv")
# print(df.info())
# print(df.head())

# dup = df.duplicated()
# for d in dup:
#     if d is True:
#         print(d)

cat_col = [d for d in df.columns if df[d].dtype=="object"]
num_col = [d for d in df.columns if df[d].dtype!="object"]
# print("Categorical cols are: ", cat_col)
# print("Numerical cols are: ", num_col)

# print(df[cat_col].nunique())
# print(df.shape)
df1 = df.drop(columns=["Name", "Ticket"])
# print(df1.shape)

print(round((df1.isnull().sum()/df.shape[0]*100),2))
print(df1.shape)
df2 = df1.drop(columns=["Cabin"])
print(df2.shape)
df2.dropna(subset=["Embarked"],axis=0,inplace=True)
print(df2.shape)
