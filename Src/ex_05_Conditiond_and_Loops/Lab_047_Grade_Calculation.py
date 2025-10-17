# Grade calculator :
# Write a program to calculate and display the program
# for given numerical score
# base on the following grade scale

# A:90-100
# B:80-89
# C:70-79
# D:60-69
# F:0-59

#Logic building formula

#1--User input score --int
#o/p -- o/p str A, B

score=int(input("Enter your score: ").strip())

if score>100 or score<= -1:
    print("You are a superman !! Ypu can't get a grade!!")
else:

    if score>=90 and score<=100:
        print("Grade is A")
    elif score>=80 and score<=89:
        print("Grade is B")
    elif score>=70 and score<=79:
        print("Grade is C")
    elif score>=60 and score<=69:
        print("Grade is D")
    else:
        print("Grade is F")



