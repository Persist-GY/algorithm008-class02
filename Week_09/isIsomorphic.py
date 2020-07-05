# https://leetcode-cn.com/problems/isomorphic-strings/

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        def helper(s1, s2):
            dic = {}
            for i in range(len(s1)):
                if s1[i] in dic and dic[s1[i]] != s2[i]:
                    return False
                else:
                    dic[s1[i]] = s2[i]
            return True
        return helper(s, t) and helper(t, s)