# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        l1 = []
        l2 = []

        def inorder(r, l):
            if r:
                l.append(r.val)
                inorder(r.left, l)
                inorder(r.right, l)
            else:
                l.append(None)
                return

        inorder(p, l1)
        inorder(q, l2)
        if l1 == l2:
            return True
        else:
            return False

