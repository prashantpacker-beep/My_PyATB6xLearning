name= ["prashant","kavinkar","qa","sdet"]

def upper_case(string):
    return string.upper()

s= upper_case("prashant")
print(s)

upper_names=list(map(upper_case,name))
print(upper_names)