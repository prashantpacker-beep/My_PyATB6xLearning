class Dog:
    name= None
    breed= None
    height= None
    weight= None

    def __init__(self):
        print("I will be called")

    def bark(self):
        print("Barking")

    def sleep(self):
        print("Sleeping")

    def talk(self):
        pass

chaw_ref= Dog()
mow_ref= Dog()

print(chaw_ref.name)
print(mow_ref.name)