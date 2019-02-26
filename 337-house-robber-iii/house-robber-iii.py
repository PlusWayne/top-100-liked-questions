# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rob(self, root: TreeNode) -> int:
        def dfs(node):
            if not node:
                return [0, 0]
            left, right = dfs(node.left), dfs(node.right)
            rob, not_rob = node.val + left[1] + right[1], max(left[0], left[1]) + max(right[0], right[1])
            return [rob, not_rob]
        return max(dfs(root))
