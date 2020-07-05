# https://leetcode-cn.com/problems/longest-valid-parentheses/solution/

class Solution:

    # 暴力
    def longestValidParentheses(self, s: str) -> int:
        def isValid(ss):
            stack = []
            for i in range(len(ss)):
                if ss[i] == '(':
                    stack.append(ss[i])
                elif stack:
                    stack.pop()
                else:
                    return False
            return len(stack) == 0
        length = 0
        for i in range(len(s)):
            for j in range(i+2, len(s)+1, 2):
                if isValid(s[i:j]):
                    length = max(length, j-i)
        return length

    def longestValidParentheses2(self, s: str) -> int:
        # 栈
        stack = [-1]
        length = 0
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                stack.pop()
                if len(stack) == 0:
                    stack.append(i)
                else:
                    length = max(length, i - stack[-1])
        return length
