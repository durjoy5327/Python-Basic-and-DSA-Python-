<<<<<<< HEAD
class HashTable:
    def __init__(self):
        self.Max= 100
        self.Arr= [None for i in range(self.Max)]

    def get_hash(self ,key):
        h=0
        for char in key:
            h+= ord(char)
        return h%self.Max

    def add( self, key, val):
        h= int(self.get_hash(key))
        self.Arr[h]=(key , val)

    def get(self, key):
        h=int(self.get_hash(key))
        return self.Arr[h]

    def delete(self, key):
        h= int(self.get_hash(key))
        self.Arr[h]=None

    def print(self):
        for item in self.Arr:
            if item is not None:
                key, val = item
                print(f'{key} = {val}')


ans= HashTable()
ans.add("march 6",380)
ans.add("march 7",400)
ans.add("march 10",280)
ans.add("march 3",480)
ans.add("march 20",200)

print(ans.get("march 6"))
ans.delete("march 3")
print(ans.Arr)
=======
class HashTable:
    def __init__(self):
        self.Max= 100
        self.Arr= [None for i in range(self.Max)]

    def get_hash(self ,key):
        h=0
        for char in key:
            h+= ord(char)
        return h%self.Max

    def add( self, key, val):
        h= int(self.get_hash(key))
        self.Arr[h]=(key , val)

    def get(self, key):
        h=int(self.get_hash(key))
        return self.Arr[h]

    def delete(self, key):
        h= int(self.get_hash(key))
        self.Arr[h]=None

    def print(self):
        for item in self.Arr:
            if item is not None:
                key, val = item
                print(f'{key} = {val}')


ans= HashTable()
ans.add("march 6",380)
ans.add("march 7",400)
ans.add("march 10",280)
ans.add("march 3",480)
ans.add("march 20",200)

print(ans.get("march 6"))
ans.delete("march 3")
print(ans.Arr)
>>>>>>> aaf52f8d7f1c5d9076e0c2db1b190b306325dddb
ans.print()