# https://leetcode-cn.com/problems/combinations/
# 回溯

class Solution():

    def combine(self, n, k):
        if n <= 0 or k <= 0 or k > n:
            return []
        self.res = []
        self.k = k
        self.n = n
        self.__dfs(1, [])
        return self.res
    
    def __dfs(self, start, pre):
        if len(pre) == self.k:
            self.res.append(pre[:])
            return
        
        for i in range(start, self.n + 2 - self.k + len(pre)):
            pre.append(i)
            self.__dfs(i + 1, pre)
            pre.pop()
