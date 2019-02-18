"""Assign to a variable in your program a triple-quoted string that contains your favorite paragraph of text -
perhaps a poem, a speech, instructions to bake a cake, some inspirational verses, etc.

Write a function that counts the number of alphabetic characters (a through z, or A through Z) in your text and then
keeps track of how many are the letter ‘e’. Your function should print an analysis of the text like this:

Your text contains 243 alphabetic characters, of which 109 (44.8%) are 'e'"""

quote = "May your heart be your guiding key."

def length():
    #letter = "e"
    number = 0

    for i in quote:
        if i == 'e':
            number = number + 1
    return number


print('Your text contains', (len(quote)), 'alphabetic characters, of which', length(), '(',((length() / len(quote) * 100)),')', 'are e.')
