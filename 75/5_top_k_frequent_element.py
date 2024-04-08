from typing import List


def topKFrequent(nums: List[int], k: int) -> List[int]:
    visited = {}

    for i in nums:
        visited[i] = visited.get(i, 0) + 1
    freq = {}
    for key, v in visited.items():
        freq[v] = freq.get(v, []) +[key]

    res = []
    print(freq)
    for i in range(len(nums), 0, -1):
        if i in freq:
            res = res + freq[i]
            if len(res) >= k:
                return res

nums = [1, 1, 1, 2, 2, 3, 3, 4]
k = 2
print(topKFrequent(nums, k))


print(topKFrequent([1], 1))
