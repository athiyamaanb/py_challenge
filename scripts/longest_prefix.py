

def common_prefix(strs):
    prefix = ""

    if len(strs) == 1:
        return strs[0]

    for i in range(len(strs[0])):

        for s in strs:
            if len(s) == i or s[i] != strs[0][i]:
                return prefix
        prefix += strs[0][i]
    return prefix



words = ["bella", "label", "roller"]
words = ["flower","flow","flight"]
words = ["flower","flower","flower","flower"]
print(common_prefix(words))