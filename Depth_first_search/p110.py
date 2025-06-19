# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def solve(r):
            if not r:
                return 0
            else:
                t1 = solve(r.left)
                t2 = solve(r.right)
                if t1 == -1 or t2 == -1 or abs(t1 - t2) > 1:
                    return -1
                else:
                    return 1 + max(t1, t2)

        temp = solve(root)
        return temp >= 0