# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res=[]
        def solve(r,sub):
            if not r:
                return
            else:
                sub.append(str(r.val))
                if not r.left and not r.right:
                    res.append('->'.join(sub))
                solve(r.left,sub)
                solve(r.right,sub)
                sub.pop()
        solve(root,[])
        return res