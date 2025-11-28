
try:
    a = int(input("Enter the number1:"))
    b = int(input("Enter the number2:"))
    c=a/b

except TypeError:
    print("Type Error")
except ZeroDivisionError:
    print("Zero division Error")
except NameError:
    print("Name Error")
except ValueError:
    print("Value Error")
else:  #it will only run if try block succeed
    print(c)
finally:
    print("I will always execute")
