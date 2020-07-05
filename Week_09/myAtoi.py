# https://leetcode-cn.com/problems/string-to-integer-atoi/

class Solution:
    def myAtoi(self, str: str) -> int:
        index = 0
        # 去前边空格
        while index < len(str) and str[index] == ' ':
            index += 1
        # 极端情况
        if index == len(str):
            return 0
        # 符号
        sign = 1
        if str[index] == '+':
            sign = 1
            index += 1
        elif str[index] == '-':
            sign = -1
            index += 1
        # 判断数字
        res = 0
        max_int = 2**31
        while index < len(str):
            if ord(str[index]) < 48 or ord(str[index]) > 57:
                break
            if res > max_int // 10 or (res == max_int // 10 and ord(str[index])-48 >= max_int % 10):
                return max_int - 1
            if res < -(max_int // 10) or (res == -(max_int // 10) and ord(str[index])-48 >= max_int % 10):
                return -max_int
            res = res*10 + sign*(ord(str[index])-48)
            index += 1
        return res