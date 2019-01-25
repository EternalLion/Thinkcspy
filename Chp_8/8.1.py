"""Add a print statement to Newton’s sqrt function that prints out better each time it is calculated.
Call your modified function with 25 as an argument and record the results."""


def newtonSqrt(n, howmany):
    approx = 0.5 * n
    for i in range(howmany):
        betterapprox = 0.5 * (approx + n / approx)
        approx = betterapprox
        print(approx, "Better")
    return betterapprox


# print(newtonSqrt(25, 3))
# print(newtonSqrt(25, 5))
print(newtonSqrt(25, 10))
