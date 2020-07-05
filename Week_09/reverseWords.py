# https://leetcode-cn.com/problems/reverse-words-in-a-string/

class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(reversed(s.split()))

    def reverseWords2(self, s):
        left, right = 0, len(s) - 1
        while left <= right and s[left] == ' ':
            left += 1
        while left <= right and s[right] == ' ':
            right -= 1
        res = []
        word = []
        while left <= right:
            if s[left] == ' ' and word:
                res.insert(0, ''.join(word))
                word = []
            elif s[left] != ' ':
                word.append(s[left])
            left += 1
        res.insert(0, ''.join(word))
        return ' '.join(res)
                 
