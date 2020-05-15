# https://leetcode-cn.com/problems/valid-perfect-square/

def isPerfectSquare(self, num):
    left, right = 1, num // 2
    while left < right:
        mid = left + (right - left + 1) // 2
        if mid * mid > num:
            right = mid - 1
        else:
            left = mid
    return left * left == num

def isPerfectSquare2(self, num):
    if num < 2:
        return True
    left = 1
    right = num // 2
    while left <= right:
        mid = left + (right - left) // 2
        sq = mid * mid
        if sq == num:
            return True
        elif sq > num:
            right = mid - 1
        else:
            left = mid + 1
    return False

def isPerfectSquare3(self, num):
    if num < 2:
        return True
    x = num // 2
    while x * x > num:
        x = (x + num / x) // 2
    return x * x == num



