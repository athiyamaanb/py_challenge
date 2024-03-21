from typing import List


# class Solution:
#     def removeElement(self, nums: List[int], val: int) -> int:
#         cleared_list = []
#         counter = 0
#         for i in nums:
#             if i == val:
#                 counter += 1
#             else:
#                 cleared_list.append(i)
#         print(len(cleared_list))
#         print(cleared_list)


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        index = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[index] = nums[i]
                index +=1
        print(nums)
        print(index)
        return index



                                

s = Solution()
s.removeElement([3,2,2,3], 3)