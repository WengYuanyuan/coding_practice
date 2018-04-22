# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        stack = []
        if root == None:
            return
        
        stack.append(root)
        while len(stack) != 0:
            current = stack.pop()
            if current.right != None:
                stack.append(current.right)
            if current.left != None:
                stack.append(current.left)
            
            current.left = None
            current.right = stack[-1] if len(stack) != 0 else None