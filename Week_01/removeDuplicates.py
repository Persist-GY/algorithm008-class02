# https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array/


class Solution():

    def removeDuplicates(self, nums):
        i = 0
        for j in range(1, len(nums)):
            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]
        print(i+1)


s = Solution()
s.removeDuplicates([0,0,1,1,1,2,2,3,3,4])