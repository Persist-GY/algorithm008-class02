# https://leetcode-cn.com/problems/burst-balloons/

from typing import List
class Solution():


    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        from functools import lru_cache
        @lru_cache(None)
        def DFS(left, right):
            if left + 1 == right: return 0
            maxNum = 0
            for i in range(left+1, right):
                current = nums[left]*nums[i]*nums[right] + DFS(left, i) + DFS(i, right)
                maxNum = max(maxNum, current)
            return maxNum
        return DFS(0, len(nums) - 1)

    def maxCoins2(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        n = len(nums)
        dp = [[0]*n for _ in range(n)]
        for left in range(n-2, -1, -1):
            for right in range(left + 2, n):
                dp[left][right] = max(nums[left]*nums[i]*nums[right] + dp[i][right] + dp[left][i] for i in range(left+1, right))
        return dp[0][n-1]