# Write a program that prints numbers from 1 to 100. However, for multiples of 3, print "Fizz" instead of the number, and for multiples of 5, print "Buzz." For numbers that are multiples of both 3 and 5, print "FizzBuzz."
# print numbers 1 to 100
# If number is multiple of 3 --- Fizz
# If number is multiple of 5 --- buzz
# If number is multiple of 3 and 5 --- Fizzbuzz


for i in range (1,101):
    if i % 3 ==0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 ==0:
        print("Fizz")
    elif i % 5 ==0:
        print("Buzz")
    else:
        print(i)

