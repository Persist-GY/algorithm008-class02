# https://leetcode-cn.com/problems/binary-tree-inorder-traversal/

class Solution():

    def inorderTraversal(self, root):
        def helper(root, res):
            if not root:
                return
            helper(root.left, res)
            res.append(root.val)
            helper(root.right, res)
        res = []
        helper(root, res)
        return res

    # 栈的思想
    def inorderTraversal2(self, root):
        res = []
        stack = []
        while len(stack) > 0 or root is not None:
            while root is not None:
                stack.append(root)
                root = root.left
            root = stack.pop()
            res.append(root.val)
            root = root.right
        return res


