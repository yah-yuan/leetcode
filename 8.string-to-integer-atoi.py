#
# @lc app=leetcode id=8 lang=python3
#
# [8] String to Integer (atoi)
#

# @lc code=start
class Solution:
    def myAtoi(self, str: str) -> int:
        e = re.search(r"^[-+]?\d+", str.lstrip())
        return max(min(int(e.group(0)), 2**31-1), -2**31) if e else 0
        
# @lc code=end

