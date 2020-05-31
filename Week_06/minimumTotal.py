# https://leetcode-cn.com/problems/triangle/

from typing import List

class Solution():

    # 自顶向下的递归
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if not triangle:
            return 0
        def DFS(row, col):
            if row == len(triangle) - 1:
                return triangle[row][col]
            left = DFS(row + 1, col)
            right = DFS(row + 1, col + 1)
            return min(left, right) + triangle[row][col]
        return DFS(0, 0)
    
    # 缓存优化
    def minimumTotal2(self, triangle: List[List[int]]) -> int:
        if not triangle:
            return 0
        from functools import lru_cache
        @lru_cache(maxsize=512)
        def DFS(row, col):
            if row == len(triangle) - 1:
                return triangle[row][col]
            left = DFS(row + 1, col)
            right = DFS(row + 1, col + 1)
            return min(left, right) + triangle[row][col]
        return DFS(0, 0)

    # 二维数组
    def minimumTotal3(self, triangle: List[List[int]]) -> int:
        if not triangle:
            return 0
        m = len(triangle)
        for i in range(m-2, -1, -1):
            for j in range(len(triangle[i])):
                triangle[i][j] += min(triangle[i+1][j], triangle[i+1][j+1])
        return triangle[0][0]

    # 一维数组
    def minimumTotal4(self, triangle: List[List[int]]) -> int:
        if not triangle:
            return 0
        m = len(triangle)
        minLen = [0 for _ in range(len(triangle[-1])+1)]
        for i in range(m-1, -1, -1):
            for j in range(len(triangle[i])):
                minLen[j] = triangle[i][j] + min(minLen[j], minLen[j+1])
        return minLen[0]
