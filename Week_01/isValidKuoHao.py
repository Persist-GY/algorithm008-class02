# https://leetcode-cn.com/problems/valid-parentheses/
# 栈的思想

class Solution():
    def isValid(self, s):
        res = []
        dic = {"{":"}", '(':')', '[':']'}
        for c in s:
            if len(res) >0 and dic[res[len(res) - 1]] == c:
                res.pop()
            else:
                if dic.get(c) == None:
                    return False
                res.append(c)
        print(len(res) == 0)

    def isValidd(self, s):
        while ("{}" in s) or ('[]' in s) or ('()' in s):
            s = s.replace('{}', '')
            s = s.replace('()', '')
            s = s.replace('[]', '')
        print(len(s) == 0)


s = Solution()
s.isValidd('{}')