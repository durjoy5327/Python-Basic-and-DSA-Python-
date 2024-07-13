class employee:
    def __init__(self , id , name):
        self.id= id
        self.name=name
    def printer(self):
        print(f"Employee id :{self.id}\nEmployee Name : {self.name}")

id = input("Enter your id please: ")
id= int(id)
name = input("Enter your name please: ")
durjoy = employee(id , name)
durjoy.printer()
print(durjoy.id)