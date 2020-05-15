# http://backstage.quchuxing.com/resources/dist/index.html#/version

def findMin(nums):
    left, right = 0, len(nums) - 1
    while left <= right:
        # 判断单个元素 否则越界
        if len(nums) == 1:
            return nums[0]
        left, right = 0, len(nums) - 1

        # 判断有序数组 否则越界
        if nums[right] > nums[left]:
            return nums[left]
        
        while left <= right:
            mid = left + (right - left) // 2
            print(mid)
            if nums[mid] > nums[mid+1]:
                return nums[mid + 1]
            if nums[mid] < nums[mid-1]:
                return nums[mid]
            if nums[mid] >= nums[0]:
                left = mid + 1
            else:
                right = mid - 1

