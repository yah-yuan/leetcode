#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        # 简单的利用栈
        extra = []
        left = ('(','[','{')
        right = {')':'(',']':'[','}':'{'}
        for i in range(len(s)):
            c = s[i]
            if c in left:
                extra.append(c)
            elif c in right:
                if extra:
                    if right[c] == extra[-1]:
                        extra.pop()
                    else:
                        return False
                else:
                    return False
            else:
                return False
        return (extra==[])

            
# @lc code=end

