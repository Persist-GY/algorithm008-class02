# https://leetcode-cn.com/problems/reverse-string-ii/

class Solution():

    def reverseStr(self, s, k):
        res = list(s)
        for i in range(0, len(s), 2*k):
            res[i:k] = reversed(res[i:k])
        return ''.join(res)