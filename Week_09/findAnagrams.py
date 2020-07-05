# https://leetcode-cn.com/problems/find-all-anagrams-in-a-string/

from typing import List
import collections


class Solution():

    def findAnagrams(self, s: str, p: str) -> List[int]:
        left, right, valid = 0, 0, 0
        need = collections.defaultdict(int)
        for c in p:
            need[c] += 1
        window = collections.defaultdict(int)
        res = []
        while right < len(s):
            c = s[right]
            right += 1
            if c in need:
                window[c] += 1
                if window[c] == need[c]:
                    valid += 1
            if right - left == len(p):
                if valid == len(need):
                    res.append(left)
                cleft = s[left]
                left += 1
                if cleft in need:
                    if window[cleft] == need[cleft]:
                        valid -= 1
                    window[cleft] -= 1
        return res
