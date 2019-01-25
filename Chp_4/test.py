import turtle


def drawSquare(t, sz):
    """Make turtle t draw a square of sz."""
    wn = turtle.Screen()
    jose = turtle.Turtle()

    for i in range(4):
        jose.forward(sz)
        jose.left(90)
