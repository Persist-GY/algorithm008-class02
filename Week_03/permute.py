# https://leetcode-cn.com/problems/permutations/

from typing import List
class Solution():

    def permute(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        self.nums = nums
        self.__dfs([], [])
        return self.res
    def __dfs(self, current, pre):
        if len(pre) == len(self.nums):
            self.res.append(pre[:])
            return
        for i, v in enumerate(self.nums):
            if i not in current:
                pre.append(v)
                current.append(i)
                self.__dfs(current, pre)
                pre.pop()
                current.pop()

    def __dfs2(self, numss, pre):
        if len(pre) == len(self.nums):
            self.res.append(pre[:])
            return
        for i, num in enumerate(numss):
            pre.append(num)
            self.__dfs2(numss[:i]+numss[i+1:], pre)
            pre.pop() 