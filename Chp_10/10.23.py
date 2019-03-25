"""Count how many words in a list have length 5."""

def countWords(lst):
    wordList = []

    for word in lst:
        if len(word) == 5:
            wordList.append(word)
    print('The word(s) in the list are: ' + str(lst))
    print('The word(s) with the length of 5 are: ' + str(wordList))
    print('Thus the number of words in the list with length of 5 is:', len(wordList))

countWords(['Sauce', 'Jackpot', 'dad', 'Upper'])