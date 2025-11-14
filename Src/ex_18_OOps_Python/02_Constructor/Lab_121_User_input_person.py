
class Person:
    name=None
    age=None
    phone=None
    occupation=None
    def __init__(self):
        print("Let's take the user input, Please share the name, age, phone no, occupation")
        self.name=input("Enter your name: \n")
        self.age=input("Enter your age:\n ")
        self.phone =input("Enter your phone no:\n")
        self.occupation=input("Enter your occupation:\n")

    def display_values(self):
        print("Name is",self.name, "Age is",self.age, "Phone No",self.phone, "Occupation is", self.occupation)

prashant=Person()
prashant.display_values()
