"""
https://leetcode-cn.com/problems/rotate-array/solution/xuan-zhuan-shu-zu-by-leetcode/
"""
# 3次旋转交换数组元素


class Solution():
    def rotateList(self, nums, k):
        k = k % len(nums)
        nums = self.rote(nums, 0, len(nums) - 1)
        nums = self.rote(nums, 0, k-1)
        nums = self.rote(nums, k, len(nums) - 1)
        print(nums)

    def rote(self, nums, start, end):
        while start < end:
            temp = nums[start]
            nums[start] = nums[end]
            nums[end] = temp
            start += 1
            end -= 1
        return nums


s = Solution()
s.rotateList([1,2,3,4,5,6,7], 3)