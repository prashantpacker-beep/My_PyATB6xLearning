#Find the number is even or odd
from operator import ifloordiv

num=int(input("Enter a number: ").strip())
if num>=0:
 if num % 2 == 0:
    print("Even")
 else:
    print("Odd")
else:
 print("Negative number")


if num>=0:
 if num % 2 == 0:
    print("Even" if num % 2 == 0 else "Odd")
else:
 print("Negative number")

 #You can write in one-liner Ternary operator

