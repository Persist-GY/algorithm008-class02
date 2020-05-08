# https://leetcode-cn.com/problems/validate-binary-search-tree/solution/yan-zheng-er-cha-sou-suo-shu-by-leetcode/

# 递归 条件没有节点 return True
# 如果当前节点小于等于最小值，或者大于等于最大值，直接return False
# 判断当前节点的左右儿子 ，更新最小值 最大值，如果有return False 直接返回
# 
class Solution():

    def isValidBST(self, root):

        def helper(node, lower = float('-inf'), upper = float('inf')):
            if not node:
                return True
            val = node.val
            if val <= lower or val >= upper:
                return False
            if not helper(node.left, lower, val):
                return False
            if not helper(node.right, val, upper):
                return False
            return True
        return helper(root)

    def isValidBST2(self, root):
        stack = [(root, float('-inf'), float('inf')), ]
        while stack:
            root, lower, upper = stack.pop()
            if not root:
                continue
            val = root.val
            if val <= lower or val >= upper:
                return False
            stack.append((root.left, lower, val))
            stack.append((root.right, val, upper))
        return True

    # 中序遍历

    def isValidBST23(self, root):

        stack, inorder = [], float('-inf')
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if root.val <= inorder:
                return False
            inorder = root.val
            root = root.right
        return True





