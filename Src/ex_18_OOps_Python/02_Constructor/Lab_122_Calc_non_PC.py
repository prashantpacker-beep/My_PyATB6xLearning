class Calc:
    a= None
    b= None

    def __init__(self):
        print("DC")

    def sum(self,a,b):
        return a+b

    def sub(self,a,b):
        return a-b

    def mult(self,a,b):
        return a*b

    def div(self,a,b):
        return a/b

a =float(input("Enter the first number a:"))
b =float(input("Enter the second number b:"))

object_ref = Calc()

output_sum = object_ref.sum(a,b)
output_sub = object_ref.sub(a,b)
output_mult = object_ref.mult(a,b)
output_div = object_ref.div(a,b)
print(output_sum,output_sub,output_mult,output_div)



