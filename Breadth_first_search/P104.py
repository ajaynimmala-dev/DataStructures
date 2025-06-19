# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        l=[]
        def solve(r,count):
            if r:
                solve(r.left,count+1)
                solve(r.right,count+1)
            else:
                l.append(count)
                return
        solve(root,0)
        return max(l)