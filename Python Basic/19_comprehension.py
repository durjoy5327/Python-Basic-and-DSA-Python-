# Comprehensions is use for converting one containter to other container
# Or same container to same container


#this is normal approach 

numbers=[1,2,3,4,5,6,7,8,9,10]
even=[]
for i in numbers:
    if i%2==0:
        even.append(i)

print("Even numbers are: ",even)


#this comprehension approach 
#odd numbers

odd=[i for i in numbers if i%2]
print("Odd numbers are: ",odd)

#square
sqr=[i*i for i in numbers]
print("Square numbers : ", sqr)


#now using set

s= set([1,2,3,4,5])
cube={i * i *i for i in s}
print(cube)

#Zip build in function where it's zipped or collab 2 list
cities=["Dhaka","New York", "Tokyo","Beijing"]
countries=["Bangladesh", "USA", "Japan","China"]
z= zip(cities,countries)
print("\nCities and countries")
for a in z:
    print(a)


#which can use another approach

d={city:country for city , country in zip(cities, countries)}
print("Cities and countries dictionary :\n",d)