# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        res = []

        def preorder(r):
            if not r:
                return
            else:
                res.append(r.val)
                preorder(r.left)
                preorder(r.right)

        if not root:
            return None
        else:
            preorder(root)
            t = root
            for i in res[1:]:
                t.left = None
                c = TreeNode(i)
                t.right = c
                t = c



