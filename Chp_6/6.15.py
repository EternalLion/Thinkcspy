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

for i in range(5):
    drawStar(tess)
    tess.penup()
    tess.forward(350)
    tess.right(144)
    tess.pendown()

wn.exitonclick()
