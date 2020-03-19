# 与3some不同，似乎只能使用2pointer而不能转化为2sum解决
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        length = len(nums)
        min_abs = abs(nums[1]+nums[2]+nums[0]-target)
        res = nums[1]+nums[2]+nums[0]
        for i in range(length):
            if i == length-2:
                break
            start = i + 1
            end = length - 1
            while start < end:
                tmp_sum = nums[start]+nums[end]+nums[i]
                tmp_abs = tmp_sum-target
                if abs(tmp_abs)<min_abs:
                    min_abs = abs(tmp_abs)
                    res = tmp_sum
                # print(i,nums[i],nums[start],nums[end],'tmp_abs:',tmp_abs,'min_abs:',min_abs)
                if tmp_abs < 0:
                    start += 1
                elif tmp_abs > 0:
                    end -= 1
                else:
                    return tmp_sum
        return res