class Dog:
    #Atrributes
    name = None
    breed = None
    height = None
    weight = None

    #Behaviour
    def bark(self):
        print("Barking")
       # print(name)
        print(self.name)
    def talk(self):
        print("Talking")

chow = Dog()
#chow--Object reference
#Dog()--Object
print(chow.name)

rancho = Dog()

