# Create a function which will take a positive number from the user and perform square of the number?

def square(number):
    if number>0:
        print(number*number)
    else:
        print("Enter a number greater than 0")

square(int(input("Enter the positive number")))
