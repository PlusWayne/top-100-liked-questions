# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root: 'TreeNode') -> 'TreeNode':
#         if root == None:
#             return None
#         temp = root.left
#         root.left = self.invertTree(root.right)
#         root.right = self.invertTree(temp)
        
#         return root
    
        if root==None:
            return
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        return root
