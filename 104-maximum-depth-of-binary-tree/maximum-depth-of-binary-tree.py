# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: 'TreeNode') -> 'int':
        res = 0
        if root == None:
            return 0
        res = 1 + max(self.maxDepth(root.left),self.maxDepth(root.right))
        
        return res
