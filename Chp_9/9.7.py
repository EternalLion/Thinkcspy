"""Write a function that mirrors its string argument, generating a string containing the original string and the
string backwards."""

def reverse(s):
    str = ""
    for i in s:
        str = i + str
    return str

print('Jackpot' + (reverse('Jackpot')))