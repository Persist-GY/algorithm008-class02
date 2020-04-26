# https://leetcode-cn.com/problems/top-k-frequent-elements/

from collections import Counter
import heapq


class Solution():
    def topFrequent(self, nums, k):
        return heapq.nlargest(k, Counter(nums).keys(), key=Counter(nums).get)
