"""Write a function that will return the number of digits in an integer."""

def numDigits(n):
    print(len(str(n)))

numDigits(120)

for i in range(100,1001):
    numDigits(i)