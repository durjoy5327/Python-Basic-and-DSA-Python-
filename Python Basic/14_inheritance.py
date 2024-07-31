class vehicle:
    def general_usage(self):
        print("General use : Transportation")

class car(vehicle):
    def __init__(self):
        print("Hello , i'm car ")
        self.wheels=4
        self.roof= True
    
    def specific_usage(self):
        self.general_usage()
        print("Specific usage : Commute word & Vacation with family")

class bike(vehicle):
    def __init__(self):
        print("Hello , i'm bike ")
        self.wheels=2
        self.roof= False
    
    def specific_usage(self):
        self.general_usage()
        print("Specific usage : Road trip & Racing")
car= car()
car.specific_usage()
print("Total wheel in car = " , car.wheels)
