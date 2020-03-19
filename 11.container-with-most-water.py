class Solution:
    def maxArea(self, height: List[int]) -> int:
        self.height = height
        return self.two_pointer()
    def two_pointer(self):
        # 两点逼近
        h = self.height
        start = 0
        end = len(h) - 1
        _max = 0
        while True:
            s = min(h[start], h[end]) * (end - start)
            if s > _max:
                _max = s
            if end - start == 1:
                return _max
            if h[start] > h[end]:
                end -= 1
            else:
                start += 1
                
    def brute_force(self):
        # 超时
        height = self.height
        length = len(height)
        max_contain = 0
        for i in range(length):
            for j in range(i,length):
                contain = min(height[i], height[j]) * (j - i)
                if contain > max_contain:
                    max_contain = contain
        return max_contain