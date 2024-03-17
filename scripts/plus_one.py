from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits_len = len(digits)
        last_num = digits[digits_len - 1]
        if digits_len == 1 and last_num + 1 > 9:
            return [int(i) for i in str(last_num+1)]
        else:
            digits[digits_len-1] = last_num + 1

        return digits


print(Solution().plusOne([1,2,3]))
print(Solution().plusOne([9]))

# 10 -> [1, 0]
# i = 10
# print([j for j in str(i)])
