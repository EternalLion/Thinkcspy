"""Write a non-fruitful function drawPoly(someturtle, somesides, somesize)
 which makes a turtle draw a regular polygon."""

import turtle


def drawPolygon(st, ss, sz):
    for i in range(sz):
        st.forward(ss)
        st.left(36)


def main():
    wn = turtle.Screen()
    wn.bgcolor("lightgreen")
    tess = turtle.Turtle()
    tess.pensize(3)
    tess.color("pink")

    drawPolygon(tess, 120, 10)  # draw a polygon

    wn.exitonclick()


main()
