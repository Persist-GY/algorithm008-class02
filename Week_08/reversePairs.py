# https://leetcode-cn.com/problems/reverse-pairs/

class Solution():


    def reversePairs(self, nums: List[int]) -> int:
        if not nums: return 0
        def mergeSort(begin, end):
            if begin >= end: return 0
            mid = (begin + end) >> 1
            count = mergeSort(begin, mid) + mergeSort(mid+1, end)
            # 合并两个数组
            i, t, c = begin, begin, 0
            cache = [0]*(end-begin+1)
            for j in range(mid+1, end+1):
                # 判断 不是反转对
                while i <= mid and nums[i] <= 2 * nums[j]: i+=1
                # 排序
                while t <= mid and nums[t] < nums[j]:
                    cache[c] = nums[t]
                    c += 1
                    t += 1
                # 临时数组放入值
                cache[c] = nums[j]
                c += 1
                # 加上 反转对
                count += mid - i + 1
            
            # 剩下部分累加到数组
            while t <= mid:
                cache[c] = nums[t]
                c += 1
                t += 1
            # 给原来的数组
            nums[begin:end+1] = cache
            return count
        return mergeSort(0, len(nums)-1)
