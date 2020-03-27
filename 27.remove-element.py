#
# @lc app=leetcode id=27 lang=python3
#
# [27] Remove Element
#

# @lc code=start
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # 遍历全部不够快!
        # i = 0
        # while i != len(nums):
        #     if nums[i] == val:
        #         nums.pop(i)
        #     else:
        #         i += 1
        # return len(nums)
        while True:
            try:
                nums.remove(val)
            except:
                break
        return len(nums)
        
# @lc code=end

s =Solution()
print()