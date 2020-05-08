# https://leetcode-cn.com/problems/subsets/
from typing import List
class Solution():

    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def helper(i, pre):
            res.append(pre[:])
            for j in range(i, len(nums)):
                pre.append(nums[j])
                helper(j + 1, pre)
                pre.pop()
        helper(0, [])
        return res

    def subsets2(self, nums):
        # 迭代
        res = [[]]
        for num in nums:
            res += [curr + [num] for curr in res]
        return res


    