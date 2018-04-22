# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        res = []
        stack = []
        if root == None:
            return res
        self.getPath(root, res, stack)
        return res
        
        
    def getPath(self, root, res, stack):
        stack.append(str(root.val))
        if root.left is None and root.right is None:            
            res.append("->".join(stack))
            stack.pop()
            return
        
        if root.left != None:
            self.getPath(root.left, res, stack)
        
        if root.right != None:
            self.getPath(root.right, res, stack)
        
        stack.pop()