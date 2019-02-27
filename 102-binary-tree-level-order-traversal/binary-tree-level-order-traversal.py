# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root != None:
            q = [root]  
        else:
            return []
        res = []
        while len(q):
            temp = []
            tt = []
            for i in q:
                tt.append(i.val)
                if i.left != None: temp.append(i.left)
                if i.right != None: temp.append(i.right) 
            q =  temp
            res.append(tt)
        return res
        
