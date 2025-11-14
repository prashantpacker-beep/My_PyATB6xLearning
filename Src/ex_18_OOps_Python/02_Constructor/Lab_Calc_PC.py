class Calc:
    a= None
    b= None
    def __init__(self,a,b):
        self.a=a
        self.b=b

    def sum(self,a,b):
        return self.a + self.b

    def sub(self,a,b):
        return self.a - self.b

    def mult(self,a,b):
        return self.a * self.b

    def div(self,a,b):
        return self.a / self.b

object_ref = Calc(3,4)
print(object_ref.sum(3,4))
print(object_ref.sub(3,4))
print(object_ref.mult(3,4))
print(object_ref.div(3,4))