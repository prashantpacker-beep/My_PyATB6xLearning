# Create a function which will take the 3 values from the user, which are length of the triangle
# trangle classifier example


side1 = float(input("Enter the first side: "))
side2 = float(input("Enter the second side: "))
side3 = float(input("Enter the third side: "))


def classify_triangle(a, b, c):
    if a > 0 and b > 0 and c > 0:
        if a + b > c and a + c > b and b + c > a:
          if a == b == c:
            return "Equilater"
          elif a == b or a == c or b == c:
            return "Isosceles"
          else:
             return "Scalene"
        else:
           print("Not a triangle")
    else:
      print("Not a valid length")
result = classify_triangle(side1, side2, side3)
print(f"The triangle is classified as: {result}")
