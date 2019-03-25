"""Create a list called myList with the following six items: 76, 92.3, “hello”, True, 4, 76.
Do it with both append and with concatenation, one item at a time."""

myList = [] #initialize list
myList.append(76)
myList.append(92.3)
myList.append("hello")
myList.append(True)
myList.append(4)
myList.append(76)
print(myList)

myList2 = []

for value in [76, 92.3, "hello", True, 4, 76]:
    myList2.append(value)

print(myList2)

