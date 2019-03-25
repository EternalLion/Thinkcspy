"""Write a function that recognizes palindromes. (Hint: use your reverse function to make this easy!)."""

def reverse(s):
    str = ""
    for i in s:
        str = i + str
    return str

def is_palindrome(myStr):
    if myStr == (reverse(myStr)):
        return True
    return False

print(is_palindrome('father'))


