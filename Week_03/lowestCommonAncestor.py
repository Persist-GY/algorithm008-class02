# https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-tree/submissions/
# 1. 递归 查找当前节点左边儿子 右边儿子是否有返回True ,判断当前节点是否是p或者q,如果有两个返回true,证明找到了
# 2. 迭代，根据父节点，把左右节点的直接父节点存入字典中，然后求得所有p的父，祖父节点放入集合，最后判断q如果不在集合中，在字典中查找q的所有父节点，最后返回q
class Solution():
    def lowestCommonAncestor(self, root, p, q):
        self.res = None
        def recurse(node):
            if not node:
                return False
            left = recurse(node.left)
            right = recurse(node.right)
            mid = node == p or node == q
            if mid + left + right == 2:
                self.res = node
            return mid or left or right
        recurse(root)
        return self.res

    def lowestCommonAncestor2(self, root, p, q):
        stack = [root]
        parent = {root: None}
        while stack:
            node = stack.pop()
            if node.left:
                stack.append(node.left)
                parent[node.left] = node
            if node.right:
                stack.append(node.right)
                parent[node.right] = node
        res = set()
        while p:
            res.add(p)
            p = parent[p]
        while q not in res:
            q = parent[q]
        return q
