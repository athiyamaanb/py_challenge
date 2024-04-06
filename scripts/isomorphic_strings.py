


def isomorphic_strings(s, t):
    forward_map = {}
    backward_map = {}
    for i in range(len(s)):
        if s[i] in forward_map:
            if forward_map[s[i]] != t[i]:
                return False
        else:
            forward_map[s[i]] = t[i]

        if t[i] in backward_map:
            if backward_map[t[i]] != s[i]:
                return False
        else:
            backward_map[t[i]] = s[i]



    # print(forward_map)
    # print(backward_map)
    return True


print(isomorphic_strings('egg', 'add'))
print(isomorphic_strings('foo', 'bar'))
print(isomorphic_strings('paper', 'title'))