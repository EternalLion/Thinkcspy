"""Sum up all the negative numbers in a list."""

def sumNegatives(lst):
    myList = []
    sum = 0
    for item in lst:
            sum = sum + item
            myList.append(item)
    print('The number of items in the list are: ' + str(abs(item)) + str(lst))
    print('The sum of the even numbers in the list is: ' + str(sum) + str(myList))

sumNegatives([-1, -2, -3  -4, -5])