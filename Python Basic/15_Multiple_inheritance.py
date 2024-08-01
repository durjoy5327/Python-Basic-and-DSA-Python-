
"""
class Father:
    def gardening(self):
        print("I love gardening")

class Mother:
    def cooking(self):
        print("I love cooking")

class child(Father, Mother):
    def sports(self):
        print("I love sports")

"""
class Father:
    def skills(self):
        print("Gardening, Programming")

class Mother:
    def skills(self):
        print("Cooking , Art")

class child(Father , Mother):
    def skills(self):
        Father.skills(self)
        Mother.skills(self)
        print("Sketching, Programming, ")



if __name__== '__main__':
    object = child()
    object.skills()