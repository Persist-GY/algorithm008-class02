# 使用二分查找，寻找一个半有序数组 [4, 5, 6, 7, 0, 1, 2] 中间无序的地方

def findUnOrder(nums):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] > nums[mid+1]:
            return mid + 1
        if nums[mid] < nums[mid-1]:
            return mid
        if nums[0] <= nums[mid]:
            left = mid + 1
        else:
            right = mid - 1