a=int(input("Enter the number1:"))
b=int(input("Enter the number2:"))
try:
  c=a/b
  print(c)
except ZeroDivisionError:
    print("Error because of the Division by zero b!=0")
