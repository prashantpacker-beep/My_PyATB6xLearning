#SET
# Collection of unique
# {}--Parenthesis

list_of_unique_elements = {1,2,3,4,4,5,5,6}
print(list_of_unique_elements)


list1 = [45.5, 33,33,45,58]
list= set(list1)
print(list)

t= ("testingacademy","for","testingacademy")
print(t)
tuple1= set(t)
print(tuple1)


mixed = {2,"QA",True, 3.14}
print(mixed)

empty= set()
print(type(empty))

for item in mixed:
    print(item)

mixed.add(4)
print(mixed)
mixed.remove(4)
print(mixed)
