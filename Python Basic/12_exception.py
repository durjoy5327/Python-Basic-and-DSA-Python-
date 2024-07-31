<<<<<<< HEAD
x= input("Enter a number : ")
y= input("Enter a number : ")

try:
    z= int(x)/ int(y)
except Exception as e:
    print('Exception occured at ',type(e).__name__) 
    z=None
=======
x= input("Enter a number : ")
y= input("Enter a number : ")

try:
    z= int(x)/ int(y)
except Exception as e:
    print('Exception occured at ',type(e).__name__) 
    z=None
>>>>>>> 10cbc65009b60475ef6701b2a2dcf71afacc3cd4
print("Division = ", z)