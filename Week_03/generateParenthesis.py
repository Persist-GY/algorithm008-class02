# https://leetcode-cn.com/problems/generate-parentheses/submissions/
# 1. 递归 先加左括号，然后右边在小于左边括号数的前提下加右括号
# 2. 结束递归条件  左括号 右括号数 都等于n
class Solution():
    
    def generateParenthesis(self, n):
        res = []
        def generate(left, right, n, s):
            if left == n and right == n:
                return res.append(s)
            if left < n:
                generate(left + 1, right, n, s + '(')
            if right < left:
                generate(left, right + 1, n, s + ')')
        generate(0, 0, n, '')
        return res