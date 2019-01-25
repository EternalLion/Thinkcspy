import turtle

# S = 3
def drawTriangle(t):
    # for i in range(S):
    for i in range(3):
        t.forward(100)
        t.left(120)


def drawOctagon(t):

    for i in range(8):
        t.forward(100)
        t.left(45)


wn = turtle.Screen()  # Set up the window
wn.bgcolor("lightgreen")

tess = turtle.Turtle()  # create tess

# drawTriangle(tess)
drawOctagon(tess)

wn.exitonclick()
