
try:
    a = int(input("Enter the number1:"))
    b = int(input("Enter the number2:"))
    c=a/b
    print(c)
except (TypeError,NameError,ValueError,ZeroDivisionError):
    print("Error due to Type, Name, Value or Zero Division")
