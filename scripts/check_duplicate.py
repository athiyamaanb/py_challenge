# Given an array of integers, find if the array contains any duplicates.
# Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.


def check_duplicate(lst):
    i = 0
    lst.sort()
    while i < len(lst)-1:# and len(lst) > 1:
        if lst[i] == lst[i+1]:
            return True
        i += 1
    return False

if __name__ == '__main__':
    input_int = [0]
    print('Input String: ')
    print(input_int)
    print('Contains Duplicates? ', check_duplicate(input_int))