# https://leetcode-cn.com/problems/zui-xiao-de-kge-shu-lcof/

import heapq

class Solution():
    def getLeastNumbers(self, arr, k):
        # 小根堆
        if len(arr) == 0 or k == 0:
            return []
        hp = [-x for x in arr[:k]]
        heapq.heapify(hp)
        for num in arr[k:]:
            heapq.heappushpop(hp, -num)
        return [-x for x in hp]