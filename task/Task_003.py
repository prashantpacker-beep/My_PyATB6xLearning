# Write python program to calculate the
#Area of the circle given its radius using the formula
# --- area= pi * r^2----(Take pi= 3.14)

#i/p---float
#o/p---string---formatted o/p of area


#Logic building formula
#stp 1
#figure it out what is input and output
# input---r--data type-- float
#pi= 3,14
#power= pow or ** any
#output --string---float--area ,print area

#step 2
#rough logic area= pi * r^2
import math

pi =3.14

radius=float(input("enter radius of circle:"))
print(radius)

#area= 3.14987654 * (radius**2)
area= math.pi *(pow(radius,2))

print("The area of the circle is ->", area)

#String data formatting
print(f"The area of the circle is -> {area:.2f}")



