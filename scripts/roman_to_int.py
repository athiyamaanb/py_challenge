lookup = {'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000}

class Solution:
    def romanToInt(self, s: str) -> int:
        sum = 0
        for i in range(0, len(s)):
            print(i)
            print(lookup[s[i]], lookup[s[i-1]])
            if i < len(s)-1 and lookup[s[i]] < lookup[s[i+1]]:
                sum -= lookup[s[i]]
                print('sub', sum)
            else:
                sum += lookup[s[i]]
                print('add', sum)
        return sum

s = Solution()
print(s.romanToInt("MCMXCIV"))