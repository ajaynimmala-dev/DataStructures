# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        l1=[]
        l2=[]
        def inorder(r,l):
            if r:
                l.append(r.val)
                inorder(r.left,l)
                inorder(r.right,l)
            else:
                l.append(None)
                return
        def secondorder(r,l):
            if r:
                l.append(r.val)
                secondorder(r.right,l)
                secondorder(r.left,l)
            else:
                l.append(None)
                return
        inorder(root.left,l1)
        secondorder(root.right,l2)
        if l1==l2:
            return True
        return False