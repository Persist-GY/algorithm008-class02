# https://leetcode-cn.com/problems/split-a-string-in-balanced-strings/

class Solution():
    def balancedStringSplit(self, s):
        res, cur = 0, 0
        for c in s:
            if c == 'L':
                cur -= 1
            else:
                cur += 1
            if cur == 0:
                res += 1
        print(res)


s = Solution()
s.balancedStringSplit("RLRRLLRLRL")
