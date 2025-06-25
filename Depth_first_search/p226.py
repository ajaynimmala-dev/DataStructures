# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.swap(root)
        return root


    def swap(self,r):
        if not r or not r.left and not r.right:
                return
        else:
            self.swap(r.left)
            self.swap(r.right)
            temp=r.left
            r.left=r.right
            r.right=temp