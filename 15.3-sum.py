# 主要是减少重复计算的方法：预处理列表，然后跳过已经进行过的3sum以及2sum
# 哈希表的使用
# 另有一个 2 pointer的解法，但都需要预处理列表
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        tmp = None
        for _ in range(len(nums)):
            target = nums.pop(0)
            if target != tmp:
                tmp = target
                res += self.twoSum(nums, -target)
                
        return res
            
    
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = {}
        res = []
        for i in range(len(nums)):
            if nums[i] in m:
                m[nums[i]].append(i)
            else:
                m[nums[i]] = [i]
        var = None
        for i in range(len(nums)):
            if nums[i] == var:
                continue
            var = nums[i]
            tmp = target-nums[i]
            if tmp in m:
                for x in m[tmp]:
                    # self and former used are not included
                    if x>i:
                        res.append([-target,nums[i],tmp])
                        break # 2sum deplicate not included so, break
        return res
    
    def threeSum(self, nums):
        # 别人写的， O(n^2)
        res = []
        nums.sort()
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l, r = i+1, len(nums)-1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s < 0:
                    l +=1 
                elif s > 0:
                    r -= 1
                else:
                    res.append((nums[i], nums[l], nums[r]))
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    l += 1; r -= 1
        return res