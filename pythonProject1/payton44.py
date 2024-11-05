# Raymund Zyron Abella, BSIT 2-B
import math

# getting the area of the triangle
base, height = 10, 12
answer1 = (base * height) / 2
print(f'The area of the triangle is: {answer1}')

# getting the surface area of a cylinder
cy_radius, cy_height = 5, 3
answer2 = 2 * math.pi * cy_radius * (cy_radius + cy_height)
print(f'the surface area of the cyclinder is: {answer2:0.02f}')
# getting the volume of the cyclinder
answer3 = math.pi * cy_radius ** 2 * cy_height
print(f'the volume of the cyclinder is: {answer3:0.02f}')

# getting the slope between two points
x1, y1 = 3, 4
x2, y2 = 5, 9
answer4 = (y2 - y1) / (x2 - x1)
print(f'the slope between two points is: {answer4}')

# getting the distance between two points
# same variables as last number
answer5 = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
print(f'the distance between two points is: {answer5:0.02f}')