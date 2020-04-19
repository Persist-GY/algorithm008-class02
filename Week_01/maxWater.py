"""
https://leetcode-cn.com/problems/container-with-most-water/

思路：
双指针，一个开头一个结尾
以开头元素与结尾元素高度最小值为判断条件
高度最小值，乘以下标差值，获得区域面积与上一个区域面积作比较取最大值
小值高度的下标，结尾减一或者开头加一,继续循环

"""
class Solution():
    def maxArea(self, nums):
        i, j, maxArea = 0, len(nums) - 1, 0
        while i < j:
            if nums[i] < nums[j]:
                maxArea = max(maxArea, nums[i]*(j-i))
                i += 1
            else:
                maxArea = max(maxArea, nums[j]*(j-i))
                j -= 1
        print(maxArea)


s = Solution()
s.maxArea([1,8,6,2,5,4,8,3,7])