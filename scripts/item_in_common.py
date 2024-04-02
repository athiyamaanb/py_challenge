
def item_in_common(list1, list2):
    items = {}

    for i in list1:
        items[i] = True

    for i in list2:
        if i in items:
            return True
    return False


print(item_in_common([1,2,3], [4,5,6]))
