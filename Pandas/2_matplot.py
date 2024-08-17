
import pandas as pd
df = pd.read_excel("F:\Python-Basic-and-DSA-Python-\Pandas\linechart.xlsx")
print(df)
from matplotlib import pyplot as plt
plt.figure(figsize=(10,5) )

#these lines are for the pie chart
total_sales = df[['Fridge', 'Dishwasher', 'Washing Machine']].sum()

plt.pie(total_sales ,labels=total_sales.index, autopct="%1.2f%%",explode=(0.05,0.5,0.05), shadow=True, startangle=120)
plt.title("Total Sales Distribution")

plt.show()

