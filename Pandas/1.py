import csv


#this is the normal approach
def calculating_rating_stats(data , industry =None ):
    ratings=[]
    for row in data:
        if row[3]!='NULL' and(not industry or row[1]==industry):
            ratings.append(float(row[3]))
    max_rating = max(ratings)
    min_rating = min(ratings)
    average_rating = sum(ratings)/len(ratings)
    return max_rating, min_rating, average_rating



file_path = r'F:\Python-Basic-and-DSA-Python-\Pandas\movies.csv'
with open(file_path, 'r') as f:
    data = list(csv.reader(f))
    header = data[0]
    data = data[1:] 
    
    max_rating ,min_rating, average_rating=calculating_rating_stats(data )
    print(f"All movies Max imdb rating is {max_rating} Minimum imdb rating is { min_rating} Average imdb rating is { average_rating} ")
    max_rating ,min_rating, average_rating=calculating_rating_stats(data,industry= "Bollywood")
    print(f"Bolloywood movies Max imdb rating is {max_rating} Minimum imdb rating is { min_rating} Average imdb rating is { average_rating} ")
    max_rating ,min_rating, average_rating=calculating_rating_stats(data,industry= "Hollywood")
    print(f"Holloywood movies Max imdb rating is {max_rating} Minimum imdb rating is { min_rating} Average imdb rating is { average_rating} ")


#Now this is the dataframe approach
import pandas as pd

df = pd.read_csv(file_path)


data_bolly =df[df.industry=="Bollywood"]
data_holly=df[df.industry=="Hollywood"]
print("Hollowood minimum rating", data_holly.imdb_rating.min() , "Maximum rating ",data_holly.imdb_rating.max(), "Average rating ",data_holly.imdb_rating.mean())
