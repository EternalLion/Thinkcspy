"""Write a function findHypot.
The function will be given the length of two sides of a right-angled triangle which should return the length of the hypotenuse.
(Hint: x ** 0.5 will return the square root, or use sqrt from the math module)"""

import math


def findHypot(a, b):
    # your code here

    # print('The two sides of the triangle are', a, 'and', b)

    hypot = (a ** 2) + (b ** 2)

    return hypot


print("The hypotenuse of the two values is", findHypot(10, 12))
print("The square root of the hypotenuse is", math.sqrt(findHypot(10, 12)))
