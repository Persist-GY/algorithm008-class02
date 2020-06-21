# https://leetcode-cn.com/problems/decode-ways/
class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0': return 0
        dp = [1] * (len(s)+1)
        for i in range(1, len(s)):
            if s[i] == '0':
                if s[i-1] == '1' or s[i-1] == '2':
                    dp[i+1] = dp[i-1]
                else:
                    return 0
            elif s[i-1] == '1':
                dp[i+1] = dp[i] + dp[i-1]
            elif s[i-1] == '2' and int(s[i]) <= 6:
                dp[i+1] = dp[i-1] + dp[i]
            else:
                dp[i+1] = dp[i]
        return dp[-1]

