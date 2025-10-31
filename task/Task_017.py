#Create a function which will take the 3 values from the user, which are length of the triangle.  side1, side2, side2
#i/p - int side1 == side2 =side3 → isoceles
#o/p = result in string - iso, eq, scalene

def length_of_the_triangle (side1, side2, side3):
    if side1==side2==side3:
        print("Triangle is Equilater")
    elif side1==side2 or side3==side2 or side3==side1:
        print("Triangle is Isocean")
    else:
        print("Triangle is Escaleno")

length_of_the_triangle(3,3,3)
length_of_the_triangle(4,4,5)
length_of_the_triangle(5,6,7)



