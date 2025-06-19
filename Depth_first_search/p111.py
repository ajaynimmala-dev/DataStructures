# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:

        def solve(r):
            if not r:
                return 0
            else:
                t1 = solve(r.left)
                t2 = solve(r.right)
                if not r.left or not r.right:
                    return 1 + max(t1, t2)
                else:
                    return 1 + min(t1, t2)

        return solve(root)