# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def dfs(node, lowB, topB):
            val = True

            if not node:
                return val
        
            if lowB >= node.val or node.val >= topB:
                val = False
            
            return val and dfs(node.left, lowB, node.val) and dfs(node.right, node.val, topB)
        
        return dfs(root, float('-inf'), float('inf'))
