# https://leetcode-cn.com/problems/wildcard-matching/
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dic = {}
        # 去除多余*
        def remove_duplicate_stars():
            if p == '':
                return p
            p1 = [p[0],]
            for x in p[1:]:
                if p1[-1] != '*' or p1[-1] == '*' and x != '*':
                    p1.append(x)
            return ''.join(p1) 
        def helper(ss, pp):
            if (ss, pp) in dic:
                return dic[(ss, pp)]
            if pp == ss or pp == '*':
                dic[(ss, pp)] = True
            elif pp == '' or ss == '':
                dic[(ss, pp)] = False
            elif pp[0] == ss[0] or pp[0] == '?':
                dic[(ss, pp)] = helper(ss[1:], pp[1:])
            elif pp[0] == '*':
                dic[(ss, pp)] = helper(ss, pp[1:]) or helper(ss[1:], pp)
            else:
                dic[(ss, pp)] = False
            return dic[(ss, pp)]
        return helper(s, remove_duplicate_stars())

