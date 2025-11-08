my_list= [1,2,3,4,5]
my_list[0]= "Prashant"
my_list[1]= "Kavinkar"

for item in my_list:
    print(item)

#range() this also return list

for i in range(1,5):
    print(i)


my_list= [1,2,3,4,5]

#indexing
print("Element at index 0 -",my_list[0])
print("Element at index 1 -",my_list[1])
print("Element at index 2 -",my_list[2])
print("Element at index 3 -",my_list[3])


# append() -- Append object to the end of the list.
my_list.append(6)
print(my_list)

my_list.append(7)
print(my_list)


#extend () --used to add another list

my_list.extend([8,9,10])
print(my_list)

#insert()-- Add perticular index

my_list.insert(1,"Prashant")
print(my_list)

my_list.insert(4,"Kavinkar")
print(my_list)

my_list.insert(0,0)
print(my_list)

my_list[2]= "Prapti"
print(my_list)

#remove --- remove perticular element
my_list.remove("Kavinkar")
print(my_list)

my_copy_list = my_list.copy()
print(my_list)
print(my_copy_list)

my_copy_list.remove("Prapti")
print(my_copy_list)