#function that return maximum value from the dictionary
# {"a":10,"b":20,"c":30}
def max_values_dict(dictionary):
#def min_values_dict (dictionary):
    return max(dictionary.values())
    #return min(dictionary.values())
def max_keys_dict(dictionary):
    return max(dictionary.keys())

print(max_values_dict({"a":10,"b":20,"c":30}))
#print(min_values_dict({"a":10,"b":20,"c":30}))
print(max_keys_dict({"a":10,"b":20,"c":30}))


