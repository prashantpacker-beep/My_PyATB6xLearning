# Remove duplicated values from a dictionary
my_dict = {"a":1, "b":2, "c":1, "d":3}

#output == {"a":1, "b":2,"d":3}

unique_values= set()
result ={}

for key, value in my_dict.items():
    if value not in unique_values:
        result[key] = value
        unique_values.add(value)

    print(result)