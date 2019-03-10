"Write a function that reverses its string argument."""

def reverse(s):
    str = ""
    for i in s:
        str = i + str
    return str

print(reverse('Jackpot'))