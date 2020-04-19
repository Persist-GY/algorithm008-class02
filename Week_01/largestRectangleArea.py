# https://leetcode-cn.com/problems/largest-rectangle-in-histogram/
# 柱状图中最大的矩形
import sys

class Solution():
    def largestRectangleArea(self, heights):
        maxArea = 0
        for i in range(len(heights)):
            minHeight = sys.maxsize
            for j in range(i, len(heights)):
                minHeight = min(minHeight, heights[j])
                maxArea = max(maxArea, minHeight * (j - i + 1))
        print(maxArea)


so = Solution()
so.largestRectangleArea([2,1,5,6,2,3])