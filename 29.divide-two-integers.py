#
# @lc app=leetcode id=29 lang=python3
#
# [29] Divide Two Integers
#

# @lc code=start
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # O(n)竟然超时了,那只有log(n)了?
        if dividend == 0:
            return 0
        op = 1
        if dividend * divisor < 0:
            op = -1
        dividend = abs(dividend)
        divisor = abs(divisor)
        rem = dividend
        res = 0
        while rem >= divisor:
            rem -= divisor
            res += 1
        return op * res
    def divide(self, dividend: int, divisor: int) -> int:
        # 尝试使用位移进行二分搜索大幅度缩小问题规模
        # 问题是怎么找到答案呢?
        # 所以不一定是缩小了问题规模, 而且可以控制成比例扩大问题因素
        MAXIMUM = 2**31 - 1
        MINIMUM = -2**31
        if not ((MINIMUM <= dividend <= MAXIMUM) and (MINIMUM <= divisor <= MAXIMUM)):
            return MAXIMUM
        if dividend == 0:
            return 0
        op = 1
        if dividend * divisor < 0:
            op = -1
        dividend = abs(dividend)
        divisor = abs(divisor)
        # if dividend < divisor:
        #     return 0
        multi = divisor
        res = 0
        while True:
            if dividend < divisor:
                res = op * res
                if not (MINIMUM <= res <= MAXIMUM):
                    return MAXIMUM
                return res
            dividend -= multi
            multi = divisor
            tmp = 1
            while True:
                multi <<= 1
                if multi < dividend:
                    tmp <<= 1
                else:
                    multi >>= 1
                    # print(dividend, multi)
                    break
            res += tmp

        

# @lc code=end

s = Solution()
print(s.divide(10, 3))
print(s.divide(-2**31, -1))
print(s.divide(21, 3))
print(s.divide(21, 2))
print(s.divide(1, 2))
print(s.divide(7, -3))