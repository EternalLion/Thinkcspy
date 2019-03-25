"""Sum up all the even numbers in a list"""

def sum_Even(lst):
    myList = []
    sum = 0
    for item in lst:
        if item % 2 == 0:
            sum = sum + item
            myList.append(item)
    print('The number of items in the list are: ' + str(item) + str(lst))
    print('The sum of the even numbers in the list is: ' + str(sum) + str(myList))

sum_Even([1, 2, 3, 4, 5])
