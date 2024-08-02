<<<<<<< HEAD

"""
This for understanding the iterator build in function work
arr=["Durjoy" ,"Karim","Abdullah","Tarek"]
itr= iter(arr)
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
"""

# Implementing iterator function

class RemoteControl:
    def __init__(self, ):
        self.channels=["HBO","Discovery","CN","Sony","Somoy Tv"]
        self.index=-1
    def __iter__(self):
        return self
    
    def __next__(self):
        self.index+=1
        if self.index==len(self.channels):
            return StopIteration
        return self.channels[self.index]

obj= RemoteControl()
itr= iter(obj)
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
=======

"""
This for understanding the iterator build in function work
arr=["Durjoy" ,"Karim","Abdullah","Tarek"]
itr= iter(arr)
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
"""

# Implementing iterator function

class RemoteControl:
    def __init__(self, ):
        self.channels=["HBO","Discovery","CN","Sony","Somoy Tv"]
        self.index=-1
    def __iter__(self):
        return self
    
    def __next__(self):
        self.index+=1
        if self.index==len(self.channels):
            return StopIteration
        return self.channels[self.index]

obj= RemoteControl()
itr= iter(obj)
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
>>>>>>> 05cbc983852d5c6a8e38e16380dbe5e439bb3ff5
print(next(itr))