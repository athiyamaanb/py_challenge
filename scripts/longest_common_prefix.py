from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        sorted_strs = sorted(strs, key=len)
        smallest = sorted_strs[0]
        for i in range(1, len(smallest)):
            # print(i)
            for str in sorted_strs[1:]:
                # print(str, smallest[:i])
                if not str.startswith(smallest[:i]):
                    break
            else:
                continue
            break

        print(smallest[:i-1])




s = Solution()
# print('test'[:0])
# print('---')
s.longestCommonPrefix(["flower","flow","flight"])
# s.longestCommonPrefix(["dog","racecar","car"])