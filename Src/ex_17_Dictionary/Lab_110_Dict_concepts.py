key=["name","role","experience"]
value=["Prashant","SDET",4]

my_dict=dict(zip(key,value))
print(my_dict)

#merge two dictionaries

dict1 = {"a":1, "b":2, "c":3}
dict2 = {"d":4, "e":5, "f":6}

merged_dict = dict1|dict2
print(merged_dict)
print(merged_dict.get("a"))
print(merged_dict.get("c"))
