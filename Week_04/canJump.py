# https://leetcode-cn.com/problems/jump-game/

# 贪心算法
def canJump(nums):
    k = 0
    for i, num in enumerate(nums):
        if i > k: return False
        k = max(k, i + num)
    return True