
squares= {x**2 for x in range(5)}
print(squares)



#frozen set (Immutable set)
# A frozen set cannot be change after creation

fset= frozenset({1,2,3,4,5,5})
print(fset)
#fset.add(6) #AttributeError: 'frozenset' object has no attribute 'add'
