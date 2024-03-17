# Smallest Substring of All Characters

# shift arr

def palindrome(s:str) -> bool:
    if len(s) == 0:
        return s
    else:
        return palindrome(s[1:]) + s[0]

n = 12214
p = palindrome(str(n))
if str(n) == p:
    print(True, p)
else:
    print(False, p)










def palindrome_int(num:int) -> bool:
    n = num
    rev = 0
    while num > 0:
        digit = num % 10 # last digit
        rev = (rev * 10) + digit
        num = num // 10
    print(rev)

    if n == rev:
        return True
    return False

print(palindrome_int(4560))







