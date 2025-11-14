a=10 #Variable which is available every where

class Person:
    b= 11 #Instance variable

    def print_info(self):
        c = 20 #Local Variable
        print(c)
        print(self.b)
        print(a)

object_ref = Person()
print(object_ref)