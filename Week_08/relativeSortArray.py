# https://leetcode-cn.com/problems/relative-sort-array/


from typing import List


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        # 计数排序
        arr = [0 for _ in range(1001)]
        ans = []
        # 把arr1 中元素对应到arr下标
        for num in arr1:
            arr[num] += 1
        # 遍历arr2 找到arr2 中元素，添加到数组，并且下标值-1
        for num in arr2:
            while arr[num] > 0:
                ans.append(num)
                arr[num] -= 1
        # arr 剩下的元素次数大于1 从小到大加入数组
        for i in range(len(arr)):
            while arr[i] > 0:
                ans.append(i)
                arr[i] -= 1
        return ans
