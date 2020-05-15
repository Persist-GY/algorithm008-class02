# https://leetcode-cn.com/problems/search-in-rotated-sorted-array/

# 保证一边是有序的 使用二分查找
def search(nums, target):
    if not nums: return -1
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid
        elif nums[0] <= nums[mid]:
            if nums[0] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if nums[mid] < target <= nums[-1]:
                left = mid + 1
            else:
                right = mid - 1
    return -1
