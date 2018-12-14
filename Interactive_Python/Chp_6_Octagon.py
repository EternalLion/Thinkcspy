import turtle


def drawSquare(t, sz):
    """Make turtle t draw a square of sz."""

    for i in range(4):
        t.forward(sz)
        t.left(45)
        t.forward(sz)
        t.left(45)


def Octagon(tx, sx):
    drawSquare(tx, sx)


wn = turtle.Screen()
tess = turtle.Turtle()

drawSquare(tess, 60)