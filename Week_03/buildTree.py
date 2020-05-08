# https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
# 递归 前序遍历第一个就是根节点，找到根节点在中序遍历中的位置，下标 + 1就是左节点个数，再截取前序遍历数组左节点数，中序遍历


class Solution():

    def buildTree(self, preorder, inorder):
        if len(inorder) == 0:
            return None
        root = TreeNode(preorder[0])
        index = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:index + 1], inorder[:index])
        root.right = self.buildTree(preorder[index + 1:], inorder[index + 1:])
        return root