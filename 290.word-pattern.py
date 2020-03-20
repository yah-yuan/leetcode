#
# @lc app=leetcode id=290 lang=python3
#
# [290] Word Pattern
#

# @lc code=start
class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        dic = {}
        str = str.split(' ')
        length = len(pattern)
        if length != len(str):
            return False
        for i in range(length):
            c = pattern[i]
            if c in dic:
                if dic[c] != str[i]:
                    return False
            else:
                if str[i] in dic.values():
                    return False
                else:
                    dic[c] = str[i]
        return True
# @lc code=end

s = Solution()
print(s.wordPattern("abba", "dog cat cat dog"))