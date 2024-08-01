
"""
try:
    raise MemoryError("Memory Error")
except MemoryError as e:
    print(e)
"""





#User define exception handling class
"""
class Accident(Exception):
    def __init__(self, msg):
        self.msg= msg
    
    def handle(self):
        print("Accient occur take a detour")

if __name__=='__main__':
    try:
        raise Accident("Two car crashes")
    except Accident as e:
        e.handle()

"""



#multiple error handling
def process_file():
    f = None 
    try:
        f = open("F:\\Python-Basic-and-DSA-Python-\\Python Basic\\info.txt")
        x = 1 / 0 
    except FileNotFoundError as e:
        print("File not found inside problem")
    finally:
        print("There is another error cleaning up file")
        if f:
            f.close()

process_file()





