squares =[1,2,9,16,25]# default--Last element
print(squares)
print(squares.pop())
print(squares)
print(squares.pop(1))
print(squares)

squares.clear()
print(squares)

# index(element,start,end)
# Return the index of the first occurance of element

numbers= [10,20,30,40,20,50]
print(numbers.index(20))

print(numbers.count(20))

numbers.sort()
print(numbers)

numbers.sort(reverse=True)
print(numbers)

numbers.reverse()
print(numbers)

#min(), max(), sum()
print(max(numbers))
print(min(numbers))
print(sum(numbers))

#slicing

print(numbers)
print(numbers[1:4]) # from index 1 to 3
print(numbers[-1])

print("apple" in numbers)
print(20 in numbers)

#List creation and comprehension

#range(1,5)--List

l= list(range(1,5))
print(l)

#nested list
matrix=[[1,2,3],[4,5,6],[7,8,9]]
print(matrix[1][2])

#delete statement---delete the index element

del numbers[0]
print(numbers)

