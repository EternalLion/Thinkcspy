"""Write a non-fruitful function to draw a five pointed star, where the length of each side is 100 units."""
import turtle
import turtle


def drawStar(t):
    angle = 144
    size = 100

    for i in range(5):
        t.forward(size)
        t.right(angle)


wn = turtle.Screen()  # Set up the window
wn.bgcolor("lightgreen")

tess = turtle.Turtle()  # create tess

drawStar(tess)

wn.exitonclick()
