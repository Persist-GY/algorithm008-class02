# https://leetcode-cn.com/problems/number-of-1-bits/

class Solution():

    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            count +=1
            n = n & (n-1) # 最低位1清0
        return count

    def hammingWeight2(self, n: int) -> int:
        count = 0
        for _ in range(32):
            if n & 1 != 0:
                count += 1
            n>>=1
        return count