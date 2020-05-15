# https://leetcode-cn.com/problems/search-a-2d-matrix/

def searchMatrix(matrix, target):
    if not matrix:
         return False
    left, right = 0, len(matrix) * len(matrix[0]) - 1
    while left <= right:
        mid = left + (right - left) // 2
        num = matrix[mid // len(matrix[0])][mid % len(matrix[0])]
        if num == target:
            return True
        elif num < target:
            left = mid + 1
        else:
            right = mid - 1
    return True
