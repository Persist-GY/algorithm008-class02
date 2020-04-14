class Solution:
    def moveZeroes(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        index = 0
        for i in range(len(nums)):
            num = nums[index]
            if num == 0:
                nums.append(num)
                nums.pop(index)
            else:
                index +=1
        return nums
solution = Solution()
print(solution.moveZeroes([1, 3, 0, 12, 4, 0]))