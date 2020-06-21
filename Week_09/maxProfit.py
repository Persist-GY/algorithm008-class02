# https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock/

class Solution():
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        for i in range(len(prices)-1):
            for j in range(i+1, len(prices)):
                ans = max(ans, prices[j]-prices[i])
        return ans
    
    def maxProfit2(self, prices: List[int]) -> int:
        n = len(prices)
        if n == 0: return 0
        dp = [0]*n
        minPrice = prices[0]
        for i in range(1, n):
            dp[i] = max(dp[i-1], prices[i]-minPrice)
            minPrice = min(minPrice, prices[i])
        return dp[-1]