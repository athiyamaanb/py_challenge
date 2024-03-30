



def fractional(num):
    if num == 1:
        return num
    return fractional(num-1) * num

print(fractional(5))