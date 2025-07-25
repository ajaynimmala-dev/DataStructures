# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res=[]
        def pre(r):
            if not r:
                return
            else:
                res.append(r.val)
                pre(r.left)
                pre(r.right)
        pre(root)
        return res