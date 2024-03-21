class Solution:

    def isHappy(self, n: int) -> bool:
        sum = 0

        for i in str(n):
            sum += int(i) ** 2

        if sum == 1:
            return True
        if sum == n**2 or sum == n:
            return False

        return self.isHappy(sum)


s = Solution()
print(s.isHappy(7))


print(7/2)
print(7//2)
print(7%2)

