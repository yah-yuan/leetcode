#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: list) -> int:
        # 为什么反而比注释里的要快??
        i = 0
        former = None
        # length = len(nums)
        while i != len(nums):
        # while i != length:
            if nums[i] == former:
                nums.pop(i)
                # length -= 1
            else:
                former = nums[i]
                i += 1
        # return length
        return len(nums)

# @lc code=end

s = Solution()
print(s.removeDuplicates([1,1,2,3,4,4,4,5]))