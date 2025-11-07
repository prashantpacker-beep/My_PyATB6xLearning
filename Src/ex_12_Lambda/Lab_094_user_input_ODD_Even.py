# write a program to calculate even /odd numbers
# def find_even_odd_num (num):
#  if num%2==0:
  #  print("Even")
  # else:
   # print("odd")

user_input=int (input("Enter a number: "))

check_even_odd_func= lambda num: "Even" if num % 2 == 0 else "Odd"
result=check_even_odd_func(user_input)
print(result)

