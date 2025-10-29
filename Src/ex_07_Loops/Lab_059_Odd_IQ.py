#for i in range(10):  # 0 to 100
    #if i % 2!=0:
        #print(i)




# Expression and result table --ERT
# | i | Condition | o/p
# | 0| 0 % 2 !=0 - False| o/p = Nothing will printed
# | 1| 1 % 2 != 0 - True | o/p = 1
# | 2| 2 % 2 !=2 - True | o/p = Nothing will printed
# | 3| 3 % 2 != 0 - False | o/p = 3


for number in range(10):
    if number % 2==0:
        continue
    else:
        print(number)