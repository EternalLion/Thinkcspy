import turtle

wn = turtle.Screen()
jose = turtle.Turtle()
jose.shape("turtle")
jose.penup()

for size in range(13):
    jose.stamp()
    jose.forward(50)
    jose.right(50)
