#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#

# @lc code=start
from copy import copy
class Solution:
    def generateParenthesis(self, n: int):
        # 回溯问题和遍历问题的区别？
        if n == 0:
            return []
        self.res = []
        self.traverse('', n, n)
        return self.res
    
    def traverse(self, s, left, right):
        if left == right == 0:
            self.res.append(s)
        if left:
            self.traverse(s+'(', left-1, right)
        if right > left:
            self.traverse(s+')', left, right-1)



# @lc code=end

s = Solution()
print(s.generateParenthesis(3))