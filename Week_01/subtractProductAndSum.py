# https://leetcode-cn.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/
# 整数n 的位数是logn,所以n对10取余的结果，加法，乘积，，，n再除以10获取前一位数字，直至n=0
class Solution():
    def subtractProductAndSum(self, n):
        add, mul = 0, 1
        while n > 0:
            num = n % 10
            add += num
            mul *= num
            n //= 10
        print(mul-add)


s = Solution()
s.subtractProductAndSum(234)