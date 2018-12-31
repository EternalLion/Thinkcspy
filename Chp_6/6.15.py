"""Draw five stars, but between each, pick up the pen, move forward by 350 units,
turn right by 144, put the pen down, and draw the next star."""
import turtle


def drawStar(t):
    angle = 144
    size = 100

    for i in range(5):
        t.forward(size)
        t.right(angle)


def main():
    wn = turtle.Screen()  # Set up the window
    wn.bgcolor("lightgreen")

    tess = turtle.Turtle()  # create tess

    for i in range(5):
        drawStar(tess)
        tess.penup()
        tess.forward(350)
        tess.right(144)
        tess.pendown()

    wn.exitonclick()


main()
