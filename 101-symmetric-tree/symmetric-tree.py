# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root == None:
            return True
        return self.isMirror(root.left,root.right)
        
        
    def isMirror(self,root1, root2):
        if root1==None and root2==None:
            return True
        if root1==None or root2==None:
            return False
        return root1.val==root2.val and self.isMirror(root1.left,root2.right) and self.isMirror(root1.right,root2.left)
