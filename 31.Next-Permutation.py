class Solution:
    def nextPermutation(self, nums: [int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        right = len(nums) - 1
        left = right - 1
        while left >= 0:
            if nums[left] < nums[left + 1]:
                while True:
                    if nums[right] > nums[left]:
                        tmp = nums[right]
                        nums[right] = nums[left]
                        nums[left] = tmp
                        break
                    right -= 1
                break
            left -= 1
        left += 1
        right = len(nums) - 1
        while left < right:
            tmp = nums[right]
            nums[right] = nums[left]
            nums[left] = tmp
            left += 1
            right -= 1
        return

if __name__ == "__main__":
    s =Solution()
    testcases = [
        ([1,2,3],[1,3,2]),
        ([3,2,1],[1,2,3]),
        ([1,1,5],[1,5,1]),
        ([1,5,4,3,2,1],[2,1,1,3,4,5]),
        ([1,3,2],[2,1,3])
    ]
    for test in testcases:
        nums = test[0]
        print(test,end='')
        s.nextPermutation(nums)
        if nums != test[1]:
            print(' error, res:',nums)
        else:
            print('')