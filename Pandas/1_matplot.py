import pandas as pd
df = pd.read_excel("F:\Python-Basic-and-DSA-Python-\Pandas\linechart.xlsx")
print(df)
from matplotlib import pyplot as plt
plt.figure(figsize=(10,5) )


# These lines for the chart
plt.title("Product Sales")
plt.plot(df["Quarter"] ,df["Fridge"],color="Maroon" , label="Fridge" )
plt.plot(df["Quarter"] ,df["Dishwasher"], label="Dishwasher1")
plt.plot(df["Quarter"] ,df["Washing Machine"] ,label="Washing Machine")
plt.xlabel('Quarter')
plt.ylabel('Values')
 
plt.legend()
plt.show()