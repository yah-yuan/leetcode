#
# @lc app=leetcode id=18 lang=python3
#
# [18] 4Sum
#

# @lc code=start
class Solution:
    def fourSum(self, nums, target: int):
        
        def threeSum(nums, t):
            # 别人写的， O(n^2)
            for i in range(len(nums)-2):
                if i > 0 and nums[i] == nums[i-1]:
                    continue
                l, r = i+1, len(nums)-1
                while l < r:
                    s = nums[i] + nums[l] + nums[r]
                    if s < t:
                        l +=1 
                    elif s > t:
                        r -= 1
                    else:
                        # print(i,l,r)
                        res.append([target-t, nums[i], nums[l], nums[r]])
                        while l < r and nums[l] == nums[l+1]:
                            l += 1
                        while l < r and nums[r] == nums[r-1]:
                            r -= 1
                        l += 1; r -= 1
        res = []
        nums.sort()
        # print(nums)
        i = 0
        while i < len(nums)-3:
            # print(nums[i+1:])
            threeSum(nums[i+1:], target-nums[i])
            while i <len(nums)-3:
                if nums[i] == nums[i+1]:
                    i+=1
                else:
                    break
            i += 1
        return res
# @lc code=end


'''
# 一个解决N-sum问题的通用解法：通过递归降低N直到变成2-Sum：
def findNsum(self, nums, target, N, result, results):
    if len(nums) < N or N < 2: return

    # solve 2-sum
    if N == 2:
        l,r = 0,len(nums)-1
        while l < r:
            if nums[l] + nums[r] == target:
                results.append(result + [nums[l], nums[r]])
                l += 1
                r -= 1
                while l < r and nums[l] == nums[l - 1]:
                    l += 1
                while r > l and nums[r] == nums[r + 1]:
                    r -= 1
            elif nums[l] + nums[r] < target:
                l += 1
            else:
                r -= 1
    else:
        for i in range(0, len(nums)-N+1):   # careful about range
            if target < nums[i]*N or target > nums[-1]*N:  # take advantages of sorted list
                break
            if i == 0 or i > 0 and nums[i-1] != nums[i]:  # recursively reduce N
                self.findNsum(nums[i+1:], target-nums[i], N-1, result+[nums[i]], results)
    return
'''