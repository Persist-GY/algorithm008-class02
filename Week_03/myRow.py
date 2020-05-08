# https://leetcode-cn.com/problems/powx-n/

class Solution():

    def myPow(self, x, n):
        def fastPow(x, N):
            if N == 0:
                return 1
            half = fastPow(x, N // 2)
            if N % 2 == 0:
                return half * half
            else:
                return half * half * x
        if n < 0:
            n = -n
            x = 1/x
        return fastPow(x, n)

    def myRow2(self, x, n):
        if n < 0:
            x = 1 / x
            n = -n
        res = 1
        current_product = x
        while n > 0:
            if n % 2 == 1:
                res *= current_product
            current_product *= current_product
            n //= 2
        return res




