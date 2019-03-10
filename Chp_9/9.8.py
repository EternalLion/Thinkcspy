"""Write a function that removes all occurrences of a given letter from a string."""
def remove_letter(theLetter, theString):
    new_string = ""
    for i in theString:
        if i != theLetter:
            new_string = new_string + i
    return new_string

print(remove_letter('a', 'banana'))