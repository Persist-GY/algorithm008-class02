"""
https://leetcode-cn.com/problems/transpose-matrix/

思路：
新创建一个数组
两个循环，赋值给相反的坐标

"""

class Solution():
    def transpose(self, A):
        R, C = len(A), len(A[0])
        ans = [[None]*R for _ in range(C)]
        for r, row in enumerate(A):
            for c, val in enumerate(row):
                ans[c][r] = val
        print(ans)


s = Solution()
s.transpose([[1,2,3],[4,5,6],[7,8,9]])