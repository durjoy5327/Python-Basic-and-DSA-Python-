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

df = pd.read_csv(r"F:\Python-Basic-and-DSA-Python-\Statistcs for Data Science & Machine learning\bhp.csv")

print(df.head())


lower_limit, upper_limit = df.price_per_sqft.quantile([0.01, 0.999])

# Remove outliers
df2 = df[(df.price_per_sqft > lower_limit) & (df.price_per_sqft < upper_limit)]
print(df2.sample(5))

#Removing outliers using 4 standard deviation
max_limit= df2.price_per_sqft.mean() + 4*df2.price_per_sqft.std()
min_limit= df2.price_per_sqft.mean() - 4*df2.price_per_sqft.std()
df3= df2[(df2.price_per_sqft>min_limit)* (df2.price_per_sqft<max_limit)]
print(df3.sample(5))


#Plot histogram
from matplotlib import pyplot as plt

sn.histplot(df3.price_per_sqft, bins=30, edgecolor='black', kde=True)
plt.title('Distribution of Price per Square Foot')
plt.xlabel('Price per square ft')
plt.ylabel('Count')
plt.grid(True)

plt.show()

#Zscore
df2['zscore']=( df2.price_per_sqft - df2.price_per_sqft.mean())/df2.price_per_sqft.std()
df4= df2[(df2.zscore>-4)& (df2.zscore<4)]
print(df4.shape)
print(df2.shape[0]-df4.shape[0])