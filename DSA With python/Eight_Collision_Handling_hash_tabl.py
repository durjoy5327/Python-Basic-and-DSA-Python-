"""import sys 
sys.path.appned("F:\Python-Basic-and-DSA-Python-\DSA With python")
from seven_hash_map_implement2 import HashTable


"""
class HashTable:
    def __init__(self):
        self.Max = 100
        self.Arr = [[] for i in range(self.Max)]

    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.Max

    def __setitem__(self, key, val):
        h = self.get_hash(key)
        found = False
        for idx, element in enumerate(self.Arr[h]):
            if len(element) == 2 and element[0] == key:
                self.Arr[h][idx] = (key, val)
                found = True
                break
        if not found:
            self.Arr[h].append((key, val))

    def __getitem__(self, key):
        h = self.get_hash(key)
        for element in self.Arr[h]:  
            if element[0] == key:
                return element[1]
        return None 

    def delete(self, key):
        h = self.get_hash(key)
        self.Arr[h] = [element for element in self.Arr[h] if element[0] != key]

    def print(self):
        for item in self.Arr:
            if item:
                for key, val in item:
                    print(f'{key} = {val}')

if __name__ == "__main__":
    ans = HashTable()
    ans["march 6"] = 380
    ans["march 7"] = 400
    ans["march 10"] = 280
    ans["march 3"] = 480
    ans["march 20"] = 200
    ans["march 17"] = 390
    print(ans["march 17"])
    ans.delete("march 3")
    ans.print() 