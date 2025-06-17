# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def inorder(r, MIN, MAX):
            if not r:
                return True
            else:
                if MAX is not None and r.val >= MAX or MIN is not None and r.val <= MIN:
                    return False
                else:
                    return inorder(r.left, MIN, r.val) and inorder(r.right, r.val, MAX)

        return inorder(root, None, None)



