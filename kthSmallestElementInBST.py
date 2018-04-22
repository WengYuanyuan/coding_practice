# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        if root != None:
            number = self.numNode(root.left) + 1
            if number == k:
                return root.val
            if number > k:
                return self.kthSmallest(root.left, k)
            else:
                return self.kthSmallest(root.right, k-number)
        
        
        
    def numNode(self, root):
        if root == None:
            return 0            
        return self.numNode(root.left) + self.numNode(root.right) + 1