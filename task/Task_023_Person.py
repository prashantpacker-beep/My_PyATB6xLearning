#Create a Person class where we will have five attributes and five behaviors. Make sure that each type of function is used, and I want you to also create the print function, which will print all the instance variable values.



class Person:
    name= "Pinki"
    age = 30
    id= "BG01"
    height= 6
    weight= 70
    occupation= "QA"

    def eat(self):
        print("I am eating")

    def talk(self,name):
        print("I am talking")
        print("I am talking",name)


    def sleep(self,name):
        print("I am sleeping")
        return None

    def walk(self):
        print("I am walking")
        return None

    def read(self):
        pass

Prashant=Person()
print(Prashant.name)
print(Prashant.age)
print(Prashant.id)
print(Prashant.height)
print(Prashant.weight)



