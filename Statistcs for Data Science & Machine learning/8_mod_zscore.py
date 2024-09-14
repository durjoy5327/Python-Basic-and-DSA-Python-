import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
df= pd.read_csv(r"F:\Python-Basic-and-DSA-Python-\Statistcs for Data Science & Machine learning\movie_revenues.csv"
                )
print(df.head(5))

_, mean,std,*_= df.revenue.describe()

def get_zscore(value,mean ,std):
    return (value-mean)/std


df['z_score']=df.revenue.apply(lambda x: get_zscore(x, mean, std))
print(df[df.z_score>3])



#modified z score
def get_mad(x):
    median= np.median(x)
    diff= np.abs(x-median)
    mad= np.median(diff)
    return mad
median= np.median(df['revenue'])
mad= get_mad(df['revenue'])
def get_mad_zscore(x, median , mad):
    return 0.6745*(x-median)/mad


df['mod_z_score']=df['revenue'].apply(lambda x: get_mad_zscore(x, median , mad))


print(df[df['mod_z_score']>3])
import seaborn as sns
top_10_revenues = df.nlargest(3, 'mod_z_score')

remove_outliters=df[df['mod_z_score']>3]
sns.barplot(x=remove_outliters['title'], y=remove_outliters['revenue'])
plt.xticks(rotation=45)
plt.show()
