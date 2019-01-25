"""The Pythagorean Theorem tells us that the length of the hypotenuse of a right triangle is related to the lengths of the other two sides.
Look through the math module and see if you can find a function that will compute this relationship for you.
Once you find it, write a short program to try it out."""

import math

x = int(input("Please give the value of one side: "))
y = int(input("Please give the value of the second side: "))

print("The hypotenuse of x and y is: ", math.hypot(x, y))
