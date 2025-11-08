cities= ("London","Paris","Madrid","Berlin")
print(len(cities))
print("Paris" in cities)
print("New York" in cities)

t= (34,45,56)
#t.append(78)--AttributeError: 'tuple' object has no attribute 'append'

ENV_API_URLs= tuple(["abc.com/ger","xyz.com/post", "qwe.com/put"])
print(ENV_API_URLs)

colors= ("red","green","blue")
for color in colors:
    print(color)

numbers= "Prashant" * 3
print(numbers)
numbers = (1,2) * 3
print(numbers)

print("---------------------------------------")

nums= (1,2,2,3,2,5)
print(len(nums))
print(nums.count(2))
print(nums.index(3))


my_list = [1,2,3,4,5]
print(my_list)
my_tuple= tuple(my_list)
print(my_tuple)

back_to_list= list(my_tuple)
print(back_to_list)
print(max(back_to_list))
print(min(back_to_list))

print("--------------------------")

my_list = [1,2,3,4,5]
print(my_list[0:2])
print(my_list[-1])

