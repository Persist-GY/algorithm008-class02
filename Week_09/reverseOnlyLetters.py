# https://leetcode-cn.com/problems/reverse-only-letters/

class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        stack = []
        res = ''
        for ss in S:
            if ss.isalpha():
                stack.append(ss)
        for ss in S:
            if ss.isalpha():
                # 是字母
                res += stack.pop()
            else:
                res += ss
        return res