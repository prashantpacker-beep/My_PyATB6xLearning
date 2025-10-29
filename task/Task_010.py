num=int(input("Enter a number which factorial you want to get:"))
fact = 1

if num<0:
    print("❌ Factorial does not exist for negative numbers.")
elif num==0:
    print("FACT: ", fact)
else:
    for i in range(1,num+1):
        fact= fact*i
    print("Factorial of number is:", fact)



