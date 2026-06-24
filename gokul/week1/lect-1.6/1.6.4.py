# 1. write a python code that takes radius of circle as input and prints the area of the circle


import math #library for mathematical caculation

radius = float(input("Enter the radius of a circle:"))

area=math.pi*radius**2

print(f"Area of the circle is {area}")