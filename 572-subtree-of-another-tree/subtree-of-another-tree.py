# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if self.isMatch(s,t):
            return True
        if s==None:
            return False
        return self.isSubtree(s.left,t) or self.isSubtree(s.right,t)
    
    
    def isMatch(self, s, t):
        if not (s and t): # s or t is none, then return
            return s == t
        return (s.val == t.val and self.isMatch(s.left, t.left) and self.isMatch(s.right, t.right))
