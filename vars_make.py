# Author: Musfirah
# Date: 2026-02-16
# This program calculates the area and perimeter of a circle, rectangle, and octagon.

# Input
circle_radius = float(input("Enter the radius of the circle: "))
rect_length = float(input("Enter the length of the rectangle: "))
rect_width = float(input("Enter the width of the rectangle: "))
octagon_side = float(input("Enter the side length of the octagon: "))

# Processing
import math

# Circle
circle_area = math.pi * circle_radius ** 2
circle_perimeter = 2 * math.pi * circle_radius

# Rectangle
rect_area = rect_length * rect_width
rect_perimeter = 2 * (rect_length + rect_width)

# Octagon
oct_area = 2 * (1 + math.sqrt(2)) * octagon_side ** 2
oct_perimeter = 8 * octagon_side

# Output
print(f"The circle has an area of {circle_area} and a perimeter of {circle_perimeter}")
print(f"The rectangle has an area of {rect_area} and a perimeter of {rect_perimeter}")
print(f"The octagon has an area of {oct_area} and a perimeter of {oct_perimeter}")