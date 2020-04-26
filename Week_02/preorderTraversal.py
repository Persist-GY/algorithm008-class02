# https://leetcode-cn.com/problems/binary-tree-preorder-traversal/

class Solution():

    def preorderTraversal(self, root):
        res = []
        def helper(root, res):
            if root == None:
                return
            res.append(root.val)
            helper(root.left, res)
            helper(root.right, res)
        helper(root, res)
        return res

    # 栈的思想
    def preorderTraversal2(self, root):
        if root == None:
            return
        stack = [root,]
        res = []
        while stack:
            root = stack.pop()
            if root is not None:
                res.append(root.val)
                if root.right is not None:
                    stack.append(root.right)
                if root.left is not None:
                    stack.append(root.left)
        return res




