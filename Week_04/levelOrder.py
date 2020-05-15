# https://leetcode-cn.com/problems/binary-tree-level-order-traversal/

class Solution():

    def levelOrder(self, root):
        # 深度优先 DFS
        levels = []
        if not root:
            return levels
        def DFS(node, level):
            if level == len(levels):
                levels.append([])
            levels[level].append(node.val)
            if node.left:
                DFS(node.left, level + 1)
            if node.right:
                DFS(node.right, level + 1)
        DFS(root, 0)
        return levels

    def levelOrder2(self, root):
        # BFS
        levels = []
        if not root:
            return levels
        queue = [root, ]
        while queue:
            size = len(queue)
            current = []
            while size > 0:
                size -= 1
                node = queue.pop(0)
                current.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            levels.append(current)
        return levels
