# https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-ii/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxPro = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                maxPro += prices[i] - prices[i-1]
        return maxPro