from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        d = deque()

        if root:
            d.append(root)

        while d:
            n = len(d)
            l = []

            for _ in range(n):
                node = d.popleft()
                l.append(node.val)
                if node.left:
                    d.append(node.left)
                if node.right:
                    d.append(node.right)

            ans.append(l)

        return ans
                