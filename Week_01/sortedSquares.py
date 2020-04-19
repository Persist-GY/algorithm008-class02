# https://leetcode-cn.com/problems/squares-of-a-sorted-array/

class Solution():
    def sortedSquares(self, nums):
        i, j = 0, len(nums) - 1
        n = j
        res = [None for _ in range(len(nums))]
        while n >= 0:
            left = nums[i] * nums[i]
            right = nums[j] * nums[j]
            if left < right:
                res[n] = right
                j -= 1
            else:
                res[n] = left
                i += 1
            n -= 1
        print(res)


s = Solution()
s.sortedSquares([-4,-1,0,3,10])