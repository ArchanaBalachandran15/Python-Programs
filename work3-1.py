# Print the Area of Circle, Rectangle, Triangle & Square
# 21/07/2025-Monday Work = 3.1

# Area of Cicle
# Area = Radius * Radius
def area_of_circle(radius):
    pi=3.14
    return pi*radius*radius
radi=float(input("Enter the radius of the circle: "))
print("Area of circle: ",area_of_circle(radi))


# Area of Rectangle 
# Area = Length * breath
def area_of_reactangle(length,breath):
    return length*breath
len=float(input("Enter the length of the Rectangle: "))
bre=float(input("Enter the width of the Rectangle: "))
print("Area of the Reactangle: ",area_of_reactangle(len,bre))


# Area of Triangle
# Area = base * height
def area_of_triangle(base,height):
    area=0.5*base*height
    return area
bas=float(input("Enter the base of the Triangle: "))
hei=float(input("Enter the width of the Triangle: "))
print("Area of the Triangle: ",area_of_triangle(bas,hei))

# Area of Square
# Area = side * side
def area_of_square(side):
    return side*side
sid=float(input("Enter the Side of the Square: "))
print("Area of the Square: ",area_of_square(sid))


