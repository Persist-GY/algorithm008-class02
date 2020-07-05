# https://leetcode-cn.com/problems/longest-palindromic-substring/

class Solution:
    def longestPalindrome(self, s: str) -> str:
        # 暴力解法  超时
        def helper(ss):
            for i in range(len(ss)):
                if ss[i] != ss[len(ss)-1-i]:
                    return False
            return True
        maxLength = 0
        maxI = 0
        maxJ = 0
        for i in range(len(s)):
            for j in range(i+1, len(s)):
                if helper(s[i:j+1]):
                    if j-i > maxLength:
                        maxLength = j - i
                        maxI = i
                        maxJ = j
        return s[maxI:maxJ+1]

    def longestPalindrome2(self, s: str) -> str:
        # 动态规划
        s2 = ''.join(reversed(list(s)))
        n = len(s)
        dp = [[0]*n for _ in range(n)]
        maxLength = 0
        maxI = 0
        for i in range(n):
            for j in range(n):
                if s[i] == s2[j]:
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = dp[i-1][j-1] + 1
                if maxLength < dp[i][j] and n-j-1+dp[i][j]-1 == i:
                    maxLength = dp[i][j]
                    maxI = i
        return s[maxI-maxLength+1:maxI+1]
