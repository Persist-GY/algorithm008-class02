# https://leetcode-cn.com/problems/valid-anagram/description/

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dic = {}
        for i in s:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1

        for j in t:
            if j in dic:
                dic[j] -= 1
                if dic[j] == 0:
                    dic.pop(j)
            
        return len(dic) == 0

    def isAnagram2(self, s, t):
        return sorted(s) == sorted(t)
