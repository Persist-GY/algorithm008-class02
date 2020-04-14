"""
给定一个由整数组成的非空数组所表示的非负整数，在该数的基础上加一。

最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。

你可以假设除了整数 0 之外，这个整数不会以零开头。

"""
# 从末尾开始遍历元素。
# 如果是9，置为0，继续下一次循环。
# 如果不是9，元素加一，直接返回数组。
# 最后如果是99， 999 ，类似这样的数，最后最头部添加元素1.
class Solution():
    
    def plusOne(self, nums):
        index = len(nums) - 1
        for i in range(len(nums)):
            if nums[index] == 9:
                nums[index] = 0
                index -=1
            else:
                nums[index] += 1
                return nums
        nums.insert(0, 1)
        return nums
            


s = Solution()
print(s.plusOne([9,9,9]))