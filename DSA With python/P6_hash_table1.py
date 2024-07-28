
"""
First we are trying to solve problem wiht list then will try to solve with 
hashtable or dictionary for better understanding differences between them....... 
here list of complexity is O(n)



stock_prices=[]
with open("F:\\Python-Basic-and-DSA-Python-\\DSA With python\\stock_prices.csv","r") as f:
    for line in f:
        token=line.split(",")
        date=token[0]
        price= float(token[1])
        stock_prices.append([date, price])

def find_price(month):
    for each in stock_prices:
        if each[0]==month:
            print(f"{month} price is : ",each[1])
            return
    print(f"Given month {month} no found")


find_price("march 8")
print(stock_prices)
"""
"""
Now we are using hashtable 

"""
stock_prices={}
with open("F:\\Python-Basic-and-DSA-Python-\\DSA With python\\stock_prices.csv","r") as f:
    for line in f:
        token=line.split(",")
        date=token[0]
        price= float(token[1])
        stock_prices[date]=price

def find_price(month):
    for each in stock_prices:
        if each[0]==month:
            print(f"{month} price is : ",each[1])
            return
    print(f"Given month {month} no found")

print(stock_prices)
print("Price of march 8 is",stock_prices[380]) 