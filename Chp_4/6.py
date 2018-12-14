    import turtle

    wn = turtle.Screen()
    tom = turtle.Turtle()

sides = int(input("How many sides do you want in the shape?"))
length = int(input("How long would you like each side to be?"))
shapecolor = input("What color would you like the shape to be?")
fill = input("What color do you want the inside of the shape to be?")

tom.color(shapecolor)
wn.bgcolor(fill)

for i in range(sides):
    tom.forward(length)
    tom.left(60)

