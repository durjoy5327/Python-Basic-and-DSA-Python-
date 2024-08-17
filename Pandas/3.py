import pandas as pd
df = pd.read_csv('F:\Python-Basic-and-DSA-Python-\Pandas\movies.csv', nrows=4)
df.to_csv('new.csv',index=False)


#excel file has multiple sheets
excel= pd.read_excel('F:\Python-Basic-and-DSA-Python-\Pandas\movies_db.xlsx', "movies")
print(excel)
