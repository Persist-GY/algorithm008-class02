
class Solution():

    def postorderTraversal(self, root):
        if root is None:
            return []
        res = []
        def helper(root, res):
            if root is None:
                return
            helper(root.left, res)
            helper(root.right, res)
            res.append(root.val)
        helper(root, res)
        return res

    def postorderTraversal2(self, root):
        if root is None: return []
        stack = [root,]
        res = []
        while stack:
            root = stack.pop()
            res.append(root.val)
            if root is not None:
                if root.left is not None:
                    stack.append(root.left)
                if root.right is not None:
                    stack.append(root.right)
        return res[::-1]
