"""
Our goal is to come up with new pandas dataframe that doesn't have 
the outliers present in it.
"""


import pandas as pd
df = pd.read_csv("F:\Python-Basic-and-DSA-Python-\Statistcs for Data Science & Machine learning\AB_NYC_2019.csv")
print(df.head(0))


print(df.price.describe())

lower_price, upper_price =df.price.quantile([0.01,0.999])

df2=df[(df.price>lower_price) & (df.price<upper_price)]
#shape is used to check how many rows and column in a dataframe
print(df2.shape)

print("\n\n\nAfter removing outliers: ")
print(df2.sample(10))