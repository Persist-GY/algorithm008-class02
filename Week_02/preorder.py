# https://leetcode-cn.com/problems/n-ary-tree-preorder-traversal/


class Solution():
    def preorder(self, root):
        if root == None:
            return []
        stack = [root, ]
        res = []
        while stack:
            root = stack.pop()
            res.append(root.val)
            stack.extend(root.children[::-1])
        return res

    def preorder2(self, root: 'Node') -> List[int]:
        res = []
        def helper(root):
            if root == None:
                return
            res.append(root.val)
            for r in root.children:
                helper(r)
        helper(root)
        return res
