# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """   
        if root == None:
            return []
        result = []
        stack = []
        stack.append(root)
        while len(stack) != 0:
            root = stack.pop()
            result.insert(0, root.val)

            if root.left != None:
                stack.append(root.left)
            if root.right != None:
                stack.append(root.right)
            
        return result
        
        
        
    
    
    
    
    
## Recursive method
#     def postorderTraversal(self, root):
#         """
#         :type root: TreeNode
#         :rtype: List[int]
#         """
#         result = []
#         self.Traversal(result, root)
#         return result
        
#     def Traversal(self, result, root):
#         if root == None:
#             return
        
#         self.Traversal(result, root.left)
#         self.Traversal(result, root.right)
#         result.append(root.val)
        
        
        
        # results = []
        # stack = []
        # current = root
        # stack.append(current)
        # while len(stack) != 0:
        #     if current.left == None and current.right == None:
        #         stack.pop(current)
        #         results.append(current.val)
        #     else:
        #         if curren.right != None:
        #             stack.append(current.right)
        #         if current.left != None:
        #             stack.append(current.left)
        #     current = stack[-1]