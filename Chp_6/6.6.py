"""Use the drawSquare function to print 5 pink squares separate from each other.
Assume each side is 20 units."""

import turtle


def drawSquare(t, sz):
    """Get turtle t to draw a square of sz side"""

    for i in range(4):
        t.forward(sz)
        t.left(90)


def main():
    wn = turtle.Screen()  # Set up the window
    wn.bgcolor("lightgreen")

    alex = turtle.Turtle()  # create alex
    alex.color("pink")
    alex.pensize(3)

    for i in range(5):
        drawSquare(alex, 20)
        alex.penup()
        alex.forward(50)
        alex.pendown()

    wn.exitonclick()


main()
