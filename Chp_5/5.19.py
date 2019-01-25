"""Search on the internet for a way to calculate an approximation for pi.
There are many that use simple arithmetic.
Write a program to compute the approximation and then print that value as well as the value of math.pi from the math module."""

import math

x = int(input("Please enter the circumference: "))
y = int(input("Please enter the diameter: "))

pi_approx = x / y

print("Your value is", pi_approx)
print("Pi is equal to", math.pi)
