# https://leetcode-cn.com/problems/jump-game-ii/

def jump(nums):
    if len(nums) == 1: return 0
    maxPosition = step = end = 0
    for i, num in enumerate(nums):
        maxPosition = max(maxPosition, i + num)
        if i == end:
            end = maxPosition
            step += 1
            if maxPosition >= len(nums) - 1:
                break
    return step


def jump2(nums):
    position = len(nums) - 1
    step = 0
    while position != 0:
        for i in range(position + 1):
            if nums[i] >= position - i:
                step += 1
                position = i
                break
    return step


