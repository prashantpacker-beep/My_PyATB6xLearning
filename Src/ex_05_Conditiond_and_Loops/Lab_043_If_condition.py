# Write a program to take user age
# let him know if can go to club
# 21

# logic building formula
# Step no 1
# i/p --age = int
# o/p--- string (Go to the club or not)

#step 2  Rough Logic
# ---
#age> 21-- Can go to club
#age<21 -- can not go to goa

#step 3 write a logic



Age = int(input("Enter the age: "))
if Age >= 21:
    print("Go to the club")
else:
    print("Not Go to the club")

#step 4 --- check for the ege case
# we should consider edge case such as
#negative ages extremely high values >-- progra,m will break
# Non-numeric input--ABC
# age which is vey high >130

#step 5 optimize code
# handle all the edge case


