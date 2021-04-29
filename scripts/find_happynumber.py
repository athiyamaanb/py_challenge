#A number is called happy if it leads to 1 after a sequence of steps where in each step number
# is replaced by sum of squares of its digit that is if we start with Happy Number and keep replacing
# it with digits square sum, we reach 1.

if __name__ == '__main__':
    max = 100
    i=1
    hpy_nmrs = []
    unhpy_nmrs  = []
    while(i<=100):
        print('Checking ' +str(i))
        j=i
        while(True):
            if j == 1:
                print(str(i) + ' is Happy Number')
                hpy_nmrs.append(i)
                break
            elif len(str(j)) == 1:
                unhpy_nmrs.append(i)
                print(str(i) + ' is NOT Happy Number')
                break
            else:
                sqrs = 0
                for chr in str(j):
                    sqrs = sqrs + (int(chr)*int(chr))
                j=sqrs
                print(sqrs)
        i += 1

    print(hpy_nmrs)
    print(unhpy_nmrs)
