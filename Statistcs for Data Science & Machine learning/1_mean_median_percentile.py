"""
Your goal is to come up with new pandas dataframe that doesn't have 
the outliers present in it.
"""


import pandas as pd
df = pd.read_csv("F:\Python-Basic-and-DSA-Python-\Statistcs for Data Science & Machine learning\AB_NYC_2019.csv")
print(df.head(0))


print(df.price.describe())

print()