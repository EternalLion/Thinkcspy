"""Write a function is_rightangled which, given the length of three sides of a triangle,
will determine whether the triangle is right-angled.
Assume that the third argument to the function is always the longest side.
It will return True if the triangle is right-angled, or False otherwise.
Hint: floating point arithmetic is not always exactly accurate, so it is not safe to test floating point numbers for equality.
If a good programmer wants to know whether x is equal or close enough to y, they would probably code it up as

if  abs(x - y) < 0.001:      # if x is approximately equal to y
    ..."""

import math

def find_hypot(a, b):
    return math.sqrt(a ** 2 + b ** 2)

def is_rightangled(a, b, c):
    if a > b and a > c:
        j, k, longest = c, b, a
    elif b > a and b > c:
        j, k, longest = c, a, b
    else:
        j, k, longest = a, b, c
    correct_hypotenuse = find_hypot(j, k)
    return abs(correct_hypotenuse - longest) < 0.001
    #return correct_hypotenuse == longest

print(find_hypot(3, 4))
print(is_rightangled(3, 4, 5))
print(is_rightangled(find_hypot(3, 5011), 3, 5011))
print(is_rightangled(12, find_hypot(12, 3), 3))
print(is_rightangled(5, 4, 3))

print(is_rightangled(12, 13, 10))