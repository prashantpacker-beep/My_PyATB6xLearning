my_dist= {
    "name": "Prashant",
    "age": 35,
    "role": "SDET",
    "exp" : 3
}
print(my_dist)
print(my_dist['age'])
print(my_dist['role'])

my_dist["role"]= "Manual Tester"
print(my_dist)

del my_dist["age"]
print(my_dist)

for key,value in my_dist.items():
    print(key,value)

print("age" in my_dist)
print("exp" in my_dist)