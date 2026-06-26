# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def dfs(p, q):

            if p is None or q is None:
                return p == q
            else:
                left_equals = dfs(p.left, q.left)
                right_equals = dfs(p.right, q.right)
            
                return left_equals and right_equals and p.val == q.val

        return dfs(p, q)


        

