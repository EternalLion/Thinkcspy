"""Write a function that removes the first occurrence of a string from another string."""

def remove(substr, theStr):
    string_remove = "the"
    sWithoutsubstr = ""

    for i in theStr:
        if i not in string_remove:
            sWithoutsubstr = sWithoutsubstr + i
    return sWithoutsubstr

print(remove('the','I make the angels scream and the devils cry'))

