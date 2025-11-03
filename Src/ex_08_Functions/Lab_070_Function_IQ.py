# Create a program for sum of three number from the user input
# if user doesn't enter any number use default as 100,200,300

# logic building
# step 1 i/p
# i/p--- int
# o/p-- int

# rough logic
# return n1+n2+n3

# write logic

num1 = int(input("enter first number\n"))
num2 = int(input("enter second number\n"))
num3 = int(input("enter third number\n"))


def sum_of_three_number(n1=100, n2=200, n3=300):
    return n1 + n2 + n3


result = sum_of_three_number(num1, num2, num3)
result1= sum_of_three_number()
result2=sum_of_three_number(n1=20, n2=30, n3=50)
result3=sum_of_three_number(n1=20, n2=30)
result4=sum_of_three_number(n1=20, n2=30, n3=num3)
result5=sum_of_three_number(n1=20)
print(result)
print(result1)
print(result2)
print(result3)
print(result4)
print(result5)
