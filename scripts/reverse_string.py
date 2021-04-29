# Write a function that reverses a string. The input string is given as an array of characters char[].
# # Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
# # You may assume all the characters consist of printable ascii characters.

def reverse_string(input_s):
    i = 0
    length = len(input_s)
    while i < length:
        input_s.append(input_s[length -1 -i])
        input_s.pop(length -1 -i)
        i += 1
    return input_s

if __name__ == '__main__':
    input_s = ['a','b','c','d']
    print('Input List: ')
    print(input_s)
    print('Reversed List: ')
    print(reverse_string(input_s))