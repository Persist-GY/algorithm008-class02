# https://leetcode-cn.com/problems/edit-distance/

class Solution():

    def minDistance(self, word1, word2):
        n1 = len(word1)
        n2 = len(word2)
        dp = [[0]*(n2+1)]*(n1+1)
        # 初始化最后一行
        for i in range(n2-1, -1, -1):
            dp[n1][i] = dp[n1][i+1] + 1
        # 初始化最后一列
        for i in range(n1-1, -1, -1):
            dp[i][n2] = dp[i+1][n2] + 1
        for i in range(n1-1, -1, -1):
            for j in range(n2-1, -1, -1):
                if word1[i] == word2[i]:
                    dp[i][j] = dp[i+1][j+1]
                else:
                    dp[i][j] = min(dp[i+1][j+1], dp[i+1][j], dp[i][j+1]) + 1
        return dp[0][0]