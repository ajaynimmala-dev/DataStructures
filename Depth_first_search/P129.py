# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def solve(r,total):
            if not r:
                return total
            else:
                if not r.left and not r.right:
                    return total*10+r.val
                elif not r.left:
                    return solve(r.right,total*10+r.val)
                elif not r.right:
                    return solve(r.left,total*10+r.val)
                else:
                    return solve(r.left,total*10+r.val)+solve(r.right,total*10+r.val)
        return solve(root,0)