



# recursion
def reverse(string: str) -> str:

    if len(string) == 0:
        return string
    else:
        print(len(string), string[1:], string[0])
        return reverse(string[1:]) + string[0]


string = 'abcdefg'
# print(string[::-1])



print(reverse(string))