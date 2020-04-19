# https://leetcode-cn.com/problems/di-yi-ge-zhi-chu-xian-yi-ci-de-zi-fu-lcof/
# python3.6 后默认字典是有序的

class Solution():
    def firstUniqChar(self, s:str):
        dic = {}
        for c in s:
            dic[c] = c in dic
        for key, v in dic.items():
            if v == False: return key
        return ' '



s = Solution()
s.firstUniqChar('leetcode')