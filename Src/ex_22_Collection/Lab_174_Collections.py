#Counter data structure

from collections import *
# user_input= input("Enter a string ")
# count_char=Counter(user_input)
# print(count_char)


#Namedtuple
# info= ('Prashant',34,True,6.1)
# print(info)
info= namedtuple('info',['name','age','ismarried','height'])
t= info('Prashant',34,True,6.1)
print(t.name)
print(t.age)
print(t.ismarried)
print(t.height)
