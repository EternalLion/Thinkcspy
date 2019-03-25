"""Sum all the elements in a list up to but not including the first even number."""

import random

def create_list():
    random_ints = []
    for _ in range(100):
        random_ints.append(random.randint(0, 1000))
    return random_ints

def sumUntilEven():
    myList = []
    lst = create_list()
    for item in lst:
        if item % 2 == 0:
            break
        myList.append(item)
    print(lst)
    print(myList)
    print(sum(myList))

sumUntilEven()
