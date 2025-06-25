# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res=[]
        def inorder(r,res):
            if not r:
                return
            else:
                inorder(r.left,res)
                res.append(r.val)
                inorder(r.right,res)
        inorder(root,res)
        return res[k-1]