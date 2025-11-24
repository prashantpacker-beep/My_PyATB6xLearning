#static method
# A static method is a method that belongs to a class rather than the instance to a class


class O:
    @staticmethod
    def sum(a,b):
        return a+b


#t=O() --- static method can be access directly.
print(O.sum(1,2))

