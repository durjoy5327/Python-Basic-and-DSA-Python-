x= input("Enter a number : ")
y= input("Enter a number : ")

try:
    z= int(x)/ int(y)
except Exception as e:
    print('Exception occured at ',type(e).__name__) 
    z=None
print("Division = ", z)