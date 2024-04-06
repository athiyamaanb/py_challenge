from typing import List


def longestConsecutive(nums: List[int]) -> int:
    set_nums = set(nums)
    longest = 0

    for i in nums:
        if i - 1 not in set_nums:
            length = 0
            while i + length in set_nums:
                length += 1
            



nums = [100, 4, 200, 1, 3, 2]
longestConsecutive(nums)
