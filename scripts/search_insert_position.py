from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target > nums[len(nums) - 1]:
            return len(nums)

        for i in range(0, len(nums)):
            if target <= nums[i]:
                return i

            elif target <= nums[i+1]:
                return i+1



s = Solution()
print(s.searchInsert([1, 3, 5, 6], 5))
print(s.searchInsert([1,3,5,6], 2))
print(s.searchInsert([1,3,5,6], 7))