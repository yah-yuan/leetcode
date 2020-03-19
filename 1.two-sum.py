'''
由于答案是唯一的，所以只需要遍历一遍即可
'''
class Solution:
    def twoSum(self, nums, target):
        m = {}
        for i in range(len(nums)):
            if target-nums[i] in m:
                return (m[target-nums[i]],i)
            else:
                m[nums[i]] = i