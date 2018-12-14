import turtle


def drawPolygon(t, sl, sd, an):
    for i in range(sd):
        t.forward(sl)
        t.left(an)


wn = turtle.Screen()
geo = turtle.Turtle()

drawPolygon(geo, 120, 10, 36)  # draw a decagon

wn.exitonclick()
