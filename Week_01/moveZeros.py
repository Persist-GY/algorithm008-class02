"""
https://leetcode-cn.com/problems/move-zeroes/
思路
遍历数组，遇到0，就删除，然后末尾追加回来。
如果元素不是0，index相应加1，进行下一个
如果是0，删除当前元素，下一个元素自动到这个0元素下标，不增加index。继续做判断

"""
class Solution():
    def moveZeroes(self, nums):
        index = 0
        for num in nums:
            if(num!=0):
                nums[index] = num
                index +=1
        while(index<len(nums)):
            nums[index] = 0
            index +=1
        return nums


s = Solution()
print(s.moveZeroes([1, 3, 0, 4, 12, 0]))
