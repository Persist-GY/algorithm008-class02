# https://leetcode-cn.com/problems/two-sum/solution/liang-shu-zhi-he-by-leetcode-2/


class Solution():


    def twoSum(self, nums, target):
        dic = {}
        for i in range(len(nums)):
            if nums[i] in dic:
                return [dic[nums[i]], i]
            else:
                dic[target- nums[i]] = i