# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.good_values = 0

        def dfs(node, maxVal):
            if node.val >= maxVal:
                self.good_values += 1

            if node.left:
                dfs(node.left, max(maxVal, node.val))
            
            if node.right:
                dfs(node.right, max(maxVal, node.val))
            
        dfs(root, float('-inf'))

        return self.good_values