def remove(substr,theStr):
    string_remove = "I"
    sWithoutsubstr = ""

    for i in theStr:
        if i != string_remove:
            sWithoutsubstr = sWithoutsubstr + i
    return sWithoutsubstr

print(remove('I', 'I am number 1. I am number 1.'))
