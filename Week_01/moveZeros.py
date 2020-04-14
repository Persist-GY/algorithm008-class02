
"""
思路
遍历数组，遇到0，就删除，然后末尾追加回来。
如果元素不是0，index相应加1，进行下一个
如果是0，删除当前元素，下一个元素自动到这个0元素下标，不增加index。继续做判断
"""

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
                nums.remove(num)
            else:
                index +=1
        return nums


solution = Solution()
print(solution.moveZeroes([1, 3, 0, 12, 4, 0]))