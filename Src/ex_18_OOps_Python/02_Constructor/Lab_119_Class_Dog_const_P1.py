print("Outside the class 1")

class Mobilephone:
    model= None

    def __init__(self):
        print("DC")

    def talk(self):
        print("Hi,Talking")

iphone = Mobilephone()
iphone.talk()

print("Outside the class 2")
