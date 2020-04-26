# https://leetcode-cn.com/problems/n-ary-tree-level-order-traversal/

class Solution:
    def levelOrder(self, root: 'Node'):
        def helper(root, level):
            if len(res) == level:
                res.append([])
            res[level].append(root.val)
            for r in root.children:
                helper(r, level+1)
        res = []
        if root != None:
            helper(root, 0)
        return res

    # 队列 广度优先搜索
    def levelOrder2(self, root):
        if root == None:
            return []
        deq = [root, ]
        res = []
        while deq:
            current = []
            res.append([])
            for r in deq:
                res[-1].append(r.val)
                current.extend(r.children)
            deq = current
        return res
