# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        results = []
        stack = []
        
        current = root
        while current != None or len(stack) != 0:
            while current != None:         
                stack.append(current)
                current = current.left
            
            current = stack.pop()
            results.append(current.val)
            current = current.right
        return results