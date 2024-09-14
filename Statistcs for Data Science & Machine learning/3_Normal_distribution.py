"""
You are given bhp.csv which contains property prices in the city of banglore, India. 
You need to examine price_per_sqft column and do following,

    1. Remove outliers using percentile technique first. Use [0.001, 0.999] for lower and upper 
    bound percentiles
    2.After removing outliers in step 1, you get a new dataframe.
    3.On step(2) dataframe, use 4 standard deviation to remove outliers
    4.Plot histogram for new dataframe that is generated after step (3). Also plot bell curve on 
    same histogram
    5.On step(2) dataframe, use zscore of 4 to remove outliers. This is quite similar to step (3) and
    you will get exact same result

"""
import pandas as pd
import seaborn as sn
df= pd.read_csv("F:\Python-Basic-and-DSA-Python-\Statistcs for Data Science & Machine learning\bhp.csv", names=["Name","Income"],skiprows=[0])

print(df.head())
