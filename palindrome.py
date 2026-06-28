def check_palindrome(string):
    if string==string[::-1]:
        return True
    return False
print(check_palindrome("madaam"))