# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        bal, depth = self.checkBalance(root)
        return bal    
        
    def checkBalance(self, root):
        if root == None:
            return True, 0
        
        bal, left_depth = self.checkBalance(root.left)
        if bal == False:
            return False, 0
        
        bal, right_depth = self.checkBalance(root.right)
        if bal == False:
            return False, 0
        
        return abs(left_depth - right_depth) <= 1, max(left_depth, right_depth) + 1
        
        

#         if root == None:
#             return True
#         stack = []
#         stack.append(root)
#         while len(stack) != 0: 
#             left_depth = self.depth(root.left)
#             right_depth = self.depth(root.right)
#             if abs(left_depth - right_depth) > 1:
#                 return False 
#             if root.right != None:
#                 stack.append(root.right)
#             if root.left != None:
#                 stack.append(root.left)
#             root = stack.pop()
#         return True
        
        
#     def depth(self, root):
#         if root == None:
#             return 0
#         return max(self.depth(root.left), self.depth(root.right)) + 1