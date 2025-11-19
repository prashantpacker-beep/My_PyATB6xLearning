# Encapsulation
#Hide the data members(Class variables, instance variables)
# By using only the method

class Car:

    def __init__(self):
        self.public_prashant="Prashant"
        self.__private_baby="Prashant@143"

    def nany(self):
        self.__private_baby="143"

object_ref= Car()
object_ref.nany()
print(object_ref.public_prashant)
print(object_ref.__private_baby)
