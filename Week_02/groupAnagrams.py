# https://leetcode-cn.com/problems/group-anagrams/


class Solution():
    def groupAnagrams(self, strs):
        ans = {}
        for s in strs:
            if ans.get(tuple(sorted(s))) == None:
                ans[tuple(sorted(s))] = []
            ans[tuple(sorted(s))].append(s)
        return list(ans.values())
