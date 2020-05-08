# https://leetcode-cn.com/problems/invert-binary-tree/

class Solution():

    def invertTree(self, root):
        # 递归
        if root == None:
            return
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
    
    def invertTree2(self, root):
        if root == None:
            return root
        # 迭代 队列
        deq = [root, ]
        while deq:
            node = deq.pop(0)
            node.left, node.right = node.right, node.left
            if node.left:
                deq.append(node.left)
            if node.right:
                deq.append(node.right)
        return root

        