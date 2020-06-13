# https://leetcode-cn.com/problems/merge-intervals/

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])# 根据最左位排序
        mergeArr = []
        for interval in intervals:
            if not mergeArr or mergeArr[-1][1] < interval[0]:
                # 不在数组 或者最大值比最小值小 直接拼接
                mergeArr.append(interval)
            else:
                # 合并两个区间
                mergeArr[-1][1] = max(mergeArr[-1][1], interval[1])
        return mergeArr