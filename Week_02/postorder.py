# https://leetcode-cn.com/problems/n-ary-tree-postorder-traversal/submissions/
class Solution:
    def postorder(self, root: 'Node'):
        if root is None:
            return []
        res = []
        stack = [root, ]
        while stack:
            root = stack.pop()
            res.append(root.val)
            stack.extend(root.children)
        res = res[::-1]
        return res