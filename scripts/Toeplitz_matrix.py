

# considers only descending columns
# traverse through row and check if column+1 is same else, return false
# repeat till row - 1

def check_toeplitx(m):
    for r in range(0, len(m[:-1])):
        for c in range(0, len(m[0])-1):
            if m[r][c] != m[r+1][c+1]:
                return False
    return True


# True
x = [[1,2,3,4],
     [5,1,2,3],
     [7,5,1,2]]
print(check_toeplitx(x))

# False
x = [[1,2,3,4],
     [5,1,9,3],
     [7,5,1,2]]
print(check_toeplitx(x))

x = []
print(check_toeplitx(x))


x = [[1,2,3,4]]
print(check_toeplitx(x))