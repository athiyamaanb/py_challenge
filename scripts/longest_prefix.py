

def common_prefix(words):
    prefix = ""
    for i in range(len(words[0])):
        for s in words:
            if len(s) == i or words[0][i] != s[i]:
                return prefix
        prefix += words[0][i]



words = ["bella", "label", "roller"]
words = ["flower","flow","flight"]
print(common_prefix(words))