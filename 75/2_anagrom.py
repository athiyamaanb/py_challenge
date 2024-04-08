def isAnagram(s: str, t: str) -> bool:
    s_visited = {}
    t_visited = {}
    if len(s) != len(t):
        return False
    for i in range(len(s)):
        if s[i] in s_visited:
            s_visited[s[i]] = s_visited.get(s[i], 0) + 1
        else:
            s_visited[s[i]] = 1
        if t[i] in t_visited:
            t_visited[t[i]] = t_visited.get(t[i], 0) + 1
        else:
            t_visited[t[i]] = 1

    for k in s_visited:
        if s_visited.get(k, 0) != t_visited.get(k, 0 ):
            return False
    return True

s = "anagram"
t = "nagaram"
s = "rat"
t = "car"
s = 'ab'
t = 'a'
print(isAnagram(s, t))