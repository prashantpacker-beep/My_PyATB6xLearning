# Frequency of character in a string
# write a program to count the frequency
# of each character in given string

string="automation"
string= input("\n Enter thr input e.g automation \n")

#{a:2,u:1,t:2,o:2,m:1,i:1,n:1}

#logic building
# i/p-> string= automation
#o/p-> dict#{a:2,u:1,t:2,o:2,m:1,i:1,n:1}

char_count = {}
for char in string:
    char_count[char] = char_count.get(char, 0) + 1
    print(char_count)