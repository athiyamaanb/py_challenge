from typing import List


def containsDuplicate(nums: List[int]) -> bool:
    visited = {}

    for i in range(len(nums)):
        if nums[i] in visited:
            return True
        else:
            visited[nums[i]] = True
    return False

nums = [1, 2, 3, 1]
nums = [1,2,3,4]
nums = [1,1,1,3,3,4,3,2,4,2]
print(containsDuplicate(nums))