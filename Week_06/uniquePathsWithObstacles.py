# https://leetcode-cn.com/problems/unique-paths-ii/

class Solution():
    def uniquePathsWithObstacles(self, obstacleGrid):
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [0 for _ in range(n)]
        iFlag = False
        jFlag = False
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    dp[j] = 0
                    if i == 0: iFlag = True
                    if j == 0: jFlag = True
                elif i == 0:
                    dp[j] = 0 if iFlag else 1
                elif j == 0:
                    dp[j] = 0 if jFlag else 1
                else:
                    dp[j] += dp[j-1]
        return dp[n-1]
