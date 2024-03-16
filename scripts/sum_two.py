from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            if i<len(nums)-1 and (nums[i] + nums[i+1]) == target:
                return [i, i+1]
        # for i, num in enumerate(nums):
        #     if nums.index(target-num) != 0:
        #         print( i, nums.index(target-num))
        #         break


s= Solution()
# s.twoSum([3,2,4], 6)
print(s.twoSum([2,7,11,15], 26))
