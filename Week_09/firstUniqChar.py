# https://leetcode-cn.com/problems/first-unique-character-in-a-string/

import collections

class Solution:
    def firstUniqChar(self, s: str) -> int:
        dic = collections.defaultdict(int)
        for i in range(len(s)):
            dic[s[i]] += 1
        for i in range(len(s)):
            if dic[s[i]] == 1:
                return i
        return -1