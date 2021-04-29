# Compress a list of elements so that it can consume less memory
# One option is to add number of repeated consecutive values eg: a,a,a -> a3

if __name__ == '__main__':
    uncmpsd_lst = [['a','a','a','b','b','c','a'],
                   ['b','b','a','a','a','c','c'],
                   ['c','d','e','f','g','h','i'],
                   ['a','a','a','a','a','a','a']]

    print('Uncompressed List:')
    for lst in uncmpsd_lst:
        print(lst)

    cmpsd_list = []
    for lst in uncmpsd_lst:
        i = 0
        counter = 1
        row = []
        while i < len(lst)-1:
            if lst[i] == lst[i+1]:
                counter += 1
                if i == len(lst)-2:
                    row.append(lst[i] + str(counter))
            else:
                row.append(lst[i]+str(counter) if counter > 1 else lst[i])
                if i == len(lst)-2:
                    row.append(lst[i+1])
                counter = 1
            i += 1

        cmpsd_list.append(row)

    print('Compressed List:')
    for lst in cmpsd_list:
        print(lst)
