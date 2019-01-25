# Use for loops to make a turtle draw these regular polygons (regular means all sides the same lengths, all angles the same):

# An equilateral triangle
# A square
# A hexagon (six sides)
# An octagon (eight sides)

import turtle

# Below is the triangle
wn = turtle.Screen()
tom = turtle.Turtle()

for i in [0, 1, 2]:
    tom.forward(60)
    tom.left(120)

# Below is the square
wn = turtle.Screen()
bob = turtle.Turtle()

for i in [0, 1, 2, 3]:
    bob.forward(50)
    bob.left(90)

# Below is the hexagon
wn = turtle.Screen()
alex = turtle.Turtle()

for i in [0, 1, 2, 3, 4, 5]:  # repeat four times
    alex.forward(60)
    alex.left(60)

# Below is the octagon
wn = turtle.Screen()
jamie = turtle.Turtle()

for i in [0, 1, 2, 3, 4, 5, 6, 7]:
    jamie.forward(45)
    jamie.left(45)
