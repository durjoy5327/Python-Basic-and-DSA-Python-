import pandas as pd
file_path = r'F:\Python-Basic-and-DSA-Python-\Pandas\movies.csv'

df = pd.read_csv(file_path)
print(df.columns)
print(df.industry.unique())
print(df.language.value_counts())
lang=df[df.language=="Bengali"]
print(lang.title)

#df_new = df[["title","industry",'imdb_rating',"release_year"]]
#print(df_new)

df_new1= df[(df.release_year>=2000) &  (df.release_year<=2010)]
print(df_new1[["title","release_year"]])


#now i want to make column which will contain the age of the movie that's mean current year minus release year

df["Age"]= df.release_year.apply(lambda x: 2024-x)
print(df)