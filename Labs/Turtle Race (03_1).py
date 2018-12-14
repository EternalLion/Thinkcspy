import turtle              # 1.  import the modules
import random
wn = turtle.Screen()       # 2.  Create a screen
wn.bgcolor('lightblue')

lance = turtle.Turtle()    # 3.  Create two turtles
andy = turtle.Turtle()
lance.color('red')
andy.color('blue')
lance.shape('turtle')
andy.shape('turtle')

andy.up()                  # 4.  Move the turtles to their starting point
lance.up()
andy.goto(-100,20)
lance.goto(-100,-20)

distance = 200 #Set up for loop range

lengthA = random.randrange(1, 10) # random call for Andy
lengthB = random.randrange(1, 10) # Random call for Lance

for i in range(distance):
    andy.forward(lengthA)
    lance.forward(lengthB)

wn.exitonclick()
