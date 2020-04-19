# https://leetcode-cn.com/problems/climbing-stairs/


class Solution():
    def climbStairs(self, n):
        f1, f2, f3 = 1, 2, 3
        for _ in range(3, n+1):
            f3 = f2 + f1
            f1 = f2
            f2 = f3
        print(f3)


s = Solution()
s.climbStairs(4)