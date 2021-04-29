# Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

def move_zeros(ele_list):
    i = j = 0
    length = len(ele_list)
    while j < length:
        if ele_list[i] == 0:
            ele_list.append(0)
            ele_list.pop(i)
        else:
            i += 1
        j += 1
        print(ele_list)

    return ele_list


if __name__ == '__main__':
    ele_list = [0, 2,0,0,1, 0]
    print('Input: ')
    print(ele_list)
    print('Output: ')
    print(move_zeros(ele_list))