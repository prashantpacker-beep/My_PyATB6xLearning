#problem find the maximum between 3 numbers

#Logic building
#user i/p num 1 , num,2, num 3
# o/p in string

num1=int(input("Enter a number:\n").strip()) #5
num2=int(input("Enter a number:\n").strip()) # 3
num3=int(input("Enter a number:\n").strip()) # 2

if num1>=num2 and num1>=num3:
    print("Max:" , num1)
elif num2>=num1 and num2>=num3:
    print("Max:" , num2)
else:
    print("Max:" , num3)

    #more than 2 conditions
