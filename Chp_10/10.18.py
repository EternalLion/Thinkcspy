"""Write a Python function that will take a the list of 100 random integers between 0 and 1000 and return the maximum value.
(Note: there is a builtin function named max but pretend you cannot use it.)"""

import random

myList = [] #initialize list

for i in range(100):
    myList.append(random.randint(0, 1001))

max_number = myList[0] #set initial max number

print(myList)

for item in myList:
    if item > max_number:
        max_number = item
    print(max_number)




