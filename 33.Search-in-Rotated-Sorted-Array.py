class Solution:
    def search(self, nums: List[int], target: int) -> int:
        right = len(nums)/2
        left = left - 1
        while left + 1 != right:
            if nums[left] >= nums[0] and nums[right] <= nums[-1]:
                break
        while left != right:
            med = (left + right) / 2
            if nums[left] < nums[right]:
                # normal
                if nums[med] == target:
                    return med
                elif nums[med] > target:
                    right = med
                else:
                    left = med
            else:
                tmp = nums[med]
                if side == 'l':
