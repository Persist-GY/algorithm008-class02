# https://leetcode-cn.com/problems/permutations-ii/

class Solution():

    def permuteUnique(self, nums):
        def __dfs(check, numss, pre):
            if len(pre) == len(nums):
                res.append(pre[:])
                return
            for i, v in enumerate(numss):
                if v in check and numss[i] == numss[i-1] and i > 0:
                    continue
                pre.append(v)
                check[v] = True
                __dfs(check, numss[:i] + numss[i+1:], pre)
                pre.pop()
        res = []
        nums.sort()
        __dfs({}, nums, [])
        return res