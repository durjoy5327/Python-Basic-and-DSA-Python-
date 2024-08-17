import pandas as pd
from matplotlib import pyplot as plt

# Read the Excel file
df = pd.read_excel("F:\Python-Basic-and-DSA-Python-\Pandas\linechart.xlsx")
print(df)

# Create the plot directly with pandas
df.plot(kind='bar', x="Quarter")
plt.xticks(rotation= 45)
plt.show()
