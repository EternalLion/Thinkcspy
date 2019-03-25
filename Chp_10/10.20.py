"""Write a function to count how many odd numbers are in a list."""

def odd_numbers(xs):
    myList = []
    for item in xs:
        if item % 2 == 1:
            myList.append(item)
    print('The odd numbers are: ' + str(myList))
    print('The numbers in the list are: ' + str(xs))

odd_numbers([1, 2, 3, 4, 5])


