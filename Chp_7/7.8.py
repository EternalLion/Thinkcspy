"""Write the function is_odd(n) that returns True when n is odd and False otherwise."""


def is_odd(n):

    if n % 2 == 1:
        return "True"
    else:
        return "False"


n = 3
print("Integer:", is_odd(n))

is_odd(n)
