# https://leetcode-cn.com/problems/power-of-two/

class Solution():

    def isPowerOfTwo(self, n):
        if n == 0: return False
        while n % 2 == 0:
            n /= 2
        return n == 1

    def isPowerOfTwo2(self, n):
        if n == 0: return False
        return n & (-n) == n # 获取最低位1  是否等于n
    
    def isPowerOfTwo3(self, n):
        if n == 0: return False
        return n & (n-1) == 0 # 删除最低位1 是否等于0