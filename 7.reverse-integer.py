class Solution:
    def reverse(self, x: int) -> int:
        x = str(x)
        if (int(x)<0) :
            x = int(x[0]+x[1::][::-1])
        else:
            x =int(x[::-1])
        return  x if -2147483648 <= x <= 2147483647 else 0 