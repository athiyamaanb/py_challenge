from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    visited = {}

    for i in range(len(nums)):
        if target - nums[i] in visited:
            return visited[target - nums[i]], i
        else:
            visited[nums[i]] = i
    return None





nums = [2,7,11,15]
target = 9
nums = [3,2,4]
target = 6

nums = [3,3]
target = 6
print(twoSum(nums, target))