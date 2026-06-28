def check_palindrome(string):
    left=0
    right=len(string)-1
    status=True
    while(left<right):
        if not string[left].isalnum():
            left+=1
            continue
        if not string[right].isalnum():
            right-=1
            continue
        if string[left].lower()==string[right].lower():
            status=True
            left+=1
            right-=1    
        else:
            status=False
            break
    return status

print(check_palindrome("aba"))