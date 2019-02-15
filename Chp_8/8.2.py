"""Write a function print_triangular_numbers(n) that prints out the first n triangular numbers.
A call to print_triangular_numbers(5) would produce the following output:

1       1
2       3
3       6
4       10
5       15
(hint: use a web search to find out what a triangular number is.)

def print_triangular_numbers(n):


    for n in range(1, n+1):
        triangular_number = n * (n + 1) / 2
        print(n, '\t', int(triangular_number))

print_triangular_numbers(5)"""

def triangular_numbers(n):
    x = 0
    for i in range(1, n + 1):
        x = x + i
        print(i, x)
    return x
triangular_numbers(5)