import pandas as pd
import seaborn as sn
from matplotlib import pyplot as plt

df = pd.read_csv(r"F:\Python-Basic-and-DSA-Python-\Statistcs for Data Science & Machine learning\revenue.csv")
print(df.head(5))

#log is use for explaining revenue in more details so that little differences can be shown breifly
df.plot(x='company', y='revenue', kind='bar', logy=True)
plt.show()

