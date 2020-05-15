# 

class Solution():

    def mySqrt(self, x):
        if x == 0:
            return x
        left = 1
        right = x // 2
        while left < right:
            mid = left + (right - left + 1) / 2
            if mid * mid > x:
                right = mid - 1
            else:
                left = mid
        return left

    def mySqrt2(self, x):
        if x == 0:
            return x
        def sqrt(y):
            res = (y + x / y) / 2
            if res == y:
                return res
            else:
                return sqrt(res)
        return int(sqrt(1))
