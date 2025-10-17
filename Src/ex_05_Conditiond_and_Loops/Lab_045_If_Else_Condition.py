#Problem to find the max between 2 numbers

#Logic building
#Step 1 .user inputs 2 integers
# o/p int which 1 is greater max will return
# or get i/p in float 31.2

num1=float(input("Enter a number: "))
num2=float(input("Enter a number: "))
if num1>0 and num2>0:
 if num1>num2:
    print("Maximum", num1)
 else:
    print("Maximum", num2)
