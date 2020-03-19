#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#

# @lc code=start
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # 事实上是树的遍历问题
        self.digits = digits
        self.phone = {'2': ['a', 'b', 'c'],
                 '3': ['d', 'e', 'f'],
                 '4': ['g', 'h', 'i'],
                 '5': ['j', 'k', 'l'],
                 '6': ['m', 'n', 'o'],
                 '7': ['p', 'q', 'r', 's'],
                 '8': ['t', 'u', 'v'],
                 '9': ['w', 'x', 'y', 'z']}
        self.length = len(digits)
        return self.traverse(0)
    def traverse(self, index):
        if index == self.length:
            return ''
        res = []
        for c in self.phone[self.digits[index]]:
            tmp = self.traverse(index+1)
            if tmp:
                for x in tmp:
                    res.append(c+x)
            else:
                res.append(c)
        return res

# @lc code=end

