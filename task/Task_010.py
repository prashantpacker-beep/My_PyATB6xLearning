from math import factorial

num=int(input("Enter a number:"))

if num<0:
    print("❌ Factorial does not exist for negative numbers.")
elif num==0:
    print("Factorial of 0 is 1")
else:
    print("Factorial is", factorial(num))



