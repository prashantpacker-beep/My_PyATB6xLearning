dict1= {"a":1, "b":2, "c":3}
print(dict1.keys())
print(dict1.values())

dict2 = {"a":1, "b":2}

# missing_keys = dict1-dict2 TypeError: unsupported operand type(s) for -: 'dict' and 'dict'
# print(missing_keys)

missing_keys = set(dict1.keys() - dict2.keys())
print(missing_keys)
