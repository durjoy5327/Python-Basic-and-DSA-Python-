class Animal:
    def __init__(self , habitat):
        self.habitat= habitat

    def print_habit(self):
        print(self.habitat)
    
    def sound(self):
        print('Some animal sound: ')

class dog(Animal):
    def __init__(self):
        super().__init__("Kennel")
    def sound(self):
        super().sound()
        print("woof woof!!")


d = dog()
d.print_habit()
d.sound()
    