# user-defined
# 1. They can't return -> non return
# 2. They can return something
# 3. They have parameters
# 4. They don't parameters/ arguments

import math

#built-in function

result = max(3,4)
print(result)

# 1. They can't return -> non return
# No return type/no parameter argument

def greet():
    print("Hello, world!")
greet()

# 2. No return type and with argument/param

def greet_by_name(name):
 print("Hello, " + name)
 greet_by_name("prashant")

# 3. No return type and with default argument ( #positional argument)

def say_hello_default_argument(name="Prashant"):
    print("Hello, " + name.upper())
say_hello_default_argument("Kavinkar")
say_hello_default_argument()

def mul_arguments(name1="A", name2="B"):
    print("Hello, " , name1, name2)
mul_arguments()
mul_arguments(name1="A", name2="B")
mul_arguments(name2="B")
mul_arguments(name1="A")
mul_arguments(name2="B", name1="A")

#def test(name):
   # print(name)
#test("test")

#Argument + Return type

def sum_of_two(a,b):
    return a+b
result = sum_of_two(3,4)
print(result)


def sum_of_two_numbers_with_defaults(num1=20,num2=30):
    print("I will sum the numbers")
    return num1+num2
result =  sum_of_two_numbers_with_defaults(num1=40,num2=50)
print(result)
result = sum_of_two_numbers_with_defaults()
print(result)

