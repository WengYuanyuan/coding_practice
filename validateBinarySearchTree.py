# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True
        BST, _, __= self.checkValid(root)
        return BST
        
    def checkValid(self, root):
        if root.left == None and root.right == None:
            return True, root.val, root.val
        if root.left == None:
            BST, max_right, min_right = self.checkValid(root.right)       
            return BST and min_right > root.val, max(max_right, root.val), min(min_right, root.val)
        if root.right == None:
            BST, max_left, min_left = self.checkValid(root.left)       
            return BST and max_left < root.val, max(max_left, root.val), min(min_left, root.val)    
        BST_left, max_right, min_right = self.checkValid(root.right)       
        BST_right, max_left, min_left = self.checkValid(root.left)       
        return BST_left and BST_right and min_right > root.val and max_left < root.val, max(max_left, max_right, root.val), min(min_left, min_right, root.val)