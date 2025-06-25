# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        def solve(r):
            if not r or r.val == p.val or r.val == q.val:
                return r
            else:
                t1 = solve(r.left)
                t2 = solve(r.right)
                if t1 and t2:
                    return r
                else:
                    return t1 if t1 else t2

        return solve(root)