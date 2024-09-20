import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
import numpy as np

df = pd.read_csv(r"F:\Python-Basic-and-DSA-Python-\Statistcs for Data Science & Machine learning\income (1).csv"
        )
print(df.sample(5))
sns.set(rc={'figure.figsize':(15,15)})
g = sns.barplot(x='income($)',y='count',data=df,palette="Spectral")
g.set_xticklabels(g.get_xticklabels(), 
                          rotation=45, 
                          horizontalalignment='right')

g.set(xscale="log")
plt.show()




