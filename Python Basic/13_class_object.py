<<<<<<< HEAD
class human:
    def __init__(self , n, o):
        self.name=n
        self.occupation=o
    
    def works(self): 
        if self.occupation.lower()=='tennis player':
            print(f"{self.name} play tennis.")
        elif self.occupation.lower()=='actor':
            print(f"{self.name} shoot film.")
        elif self.occupation.lower()== 'singer':
            print(f"{self.name} sing song.")
    def speaks(self):
        print(self.name, "says hello there!!")


durjoy= human("Durjoy" , "Actor")
durjoy.works()
durjoy.speaks()

joya= human("Joya" ,'singer')
joya.works()
=======
class human:
    def __init__(self , n, o):
        self.name=n
        self.occupation=o
    
    def works(self): 
        if self.occupation.lower()=='tennis player':
            print(f"{self.name} play tennis.")
        elif self.occupation.lower()=='actor':
            print(f"{self.name} shoot film.")
        elif self.occupation.lower()== 'singer':
            print(f"{self.name} sing song.")
    def speaks(self):
        print(self.name, "says hello there!!")


durjoy= human("Durjoy" , "Actor")
durjoy.works()
durjoy.speaks()

joya= human("Joya" ,'singer')
joya.works()
>>>>>>> 10cbc65009b60475ef6701b2a2dcf71afacc3cd4
joya.speaks()