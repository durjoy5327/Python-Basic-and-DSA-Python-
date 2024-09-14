<<<<<<< HEAD
import pandas as pd
import numpy as np

df= pd.read_csv("F:\Python-Basic-and-DSA-Python-\Statistcs for Data Science & Machine learning\income.csv", names=["Name","Income"],skiprows=[0])

print(df.Income.describe())
print(df.Income.quantile(0))
print(df.Income.quantile(0.99 , interpolation="higher" ))

#lets make a value in income column NAN then we will filled it will mean
df.Income[3]=np.nan
print(df)
df.fillna(df['Income'].mean(), inplace=True)
print("Here I use mean in place of NaN:")
print(df)

# Now, fill NaN values with the median (reset the specific cell to NaN again for demonstration)
df.loc[3, 'Income'] = np.nan
df.fillna(df['Income'].median(), inplace=True)
print("Here I use median in place of NaN:")
print(df)

=======
import pandas as pd
import numpy as np

df= pd.read_csv("F:\Python-Basic-and-DSA-Python-\Statistcs for Data Science & Machine learning\income.csv", names=["Name","Income"],skiprows=[0])

print(df.Income.describe())
print(df.Income.quantile(0))
print(df.Income.quantile(0.99 , interpolation="higher" ))

#lets make a value in income column NAN then we will filled it will mean
df.Income[3]=np.nan
print(df)
df.fillna(df['Income'].mean(), inplace=True)
print("Here I use mean in place of NaN:")
print(df)

# Now, fill NaN values with the median (reset the specific cell to NaN again for demonstration)
df.loc[3, 'Income'] = np.nan
df.fillna(df['Income'].median(), inplace=True)
print("Here I use median in place of NaN:")
print(df)

>>>>>>> 6e7d3dbbe24263c3b15965585e6b69f34f465a2b
