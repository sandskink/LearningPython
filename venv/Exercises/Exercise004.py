#Exercises from https://www.w3resource.com/python-exercises/python-basic-exercises.php
#Write a Python program which accepts the radius of a circle from the user and compute the area
import math
radius = float(input("Enter the radius of a circle"))
print(type(radius))
area = math.pi*math.pow(radius,2)
print("The area of this circle is "+format(area))