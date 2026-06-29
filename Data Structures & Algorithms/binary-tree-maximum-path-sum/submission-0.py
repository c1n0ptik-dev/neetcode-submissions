# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxPath = float('-inf')

        def helper(node):
            if not node:
                return 0

            left = max(0, helper(node.left))
            right = max(0, helper(node.right))

            maxLocalPath = max(node.val, node.val + left, node.val + right)
            maxChildPath = maxLocalPath

            if left + node.val + right > maxLocalPath:
                maxLocalPath = left + node.val + right

            self.maxPath = max(self.maxPath, maxLocalPath)

            return maxChildPath

        helper(root)

        return self.maxPath


            
                


            