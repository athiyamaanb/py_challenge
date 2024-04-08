from typing import List

# Bruteforce method
# time complexity is o(n^2)
# space complexity is o(n)
def productExceptSelf(nums: List[int]) -> List[int]:
    res = []
    for i in range(1, len(nums)+1):
        p_res = 1
        for j in range(1, len(nums)+1):
            if i != j:
                print(i, j, p_res)
                p_res *= nums[j-1]

        res.append(p_res)
    return res

# nums = [1,2,3,4]
nums = [-1,1,0,-3,3]
print(productExceptSelf(nums))