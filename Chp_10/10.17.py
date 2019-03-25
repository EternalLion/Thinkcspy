"""Create a list containing 100 random integers between 0 and 1000 (use iteration, append, and the random module).
Write a function called average that will take the list as a parameter and return the average."""

import random

myList = []

for i in range(100):
    myList.append(random.randint(0, 1000))

print(myList)

def average():
    sum = 0
    for item in myList:
        sum = sum + item
    print(sum)
    print(sum / len(myList))


average()
