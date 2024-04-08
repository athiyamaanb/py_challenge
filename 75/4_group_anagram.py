from collections import defaultdict
from typing import List


def groupAnagrams(strs: List[str]) -> List[List[str]]:

    res = {}
    for s in strs:
        c_map = [0] * 26
        for c in s:
            c_map[ord(c) - ord('a')] += 1
        key = tuple(c_map)
        res[key] = res.get(key, []) + [s]

    return list(res.values())

strs = ["eat","tea","tan","ate","nat","bat"]
print(groupAnagrams(strs))