class Dog:
    #Attribute ---Instance variable/ Data Variable

    name= None
    breed= None
    height= None
    weight= None
    race= None

    def __init__(self,nameGiven,breedGiven):
            print("Param C")
            self.name = nameGiven
            self.breed = breedGiven


    #Bahaviour
    def bark(self):
        print("Hi,barking")

    def sleep(self):
        print("Who is sleeping--> ", self.name)

    def talk(self):
        pass

chaw= Dog("chaw","mastiff")
rancho= Dog("rancho","desi")

chaw.sleep()
rancho.sleep()
