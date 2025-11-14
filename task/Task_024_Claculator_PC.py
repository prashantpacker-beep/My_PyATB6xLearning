# You need to create a calculator function, but the calculator function has to take the value from the parameterized constructor. So while creating the object, you will pass the parameters and that will basically return the sum of the two numbers, multiplication of two numbers



class Calc:
    a = None
    b = None

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def sum(self):
        return self.a + self.b

    def sub(self):
        return self.a - self.b

    def mul(self):
        return self.a * self.b

    def div(self):
        return self.a / self.b

calculator = Calc(3, 2)
print(calculator.sum())
print(calculator.sub())
print(calculator.mul())
print(calculator.div())