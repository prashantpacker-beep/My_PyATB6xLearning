
try:
    a = int(input("Enter the number1:"))
    b = int(input("Enter the number2:"))
    c=a/b
    print(c)
except TypeError:
    print("Type Error")
except ZeroDivisionError:
    print("Zero division Error")
except NameError:
    print("Name Error")
except ValueError:
    print("Value Error")
