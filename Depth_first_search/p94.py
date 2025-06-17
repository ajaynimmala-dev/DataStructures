# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        sub = []

        def inorder(root):
            if root == None:
                return
            else:
                inorder(root.left)
                sub.append(root.val)
                inorder(root.right)

        inorder(root)
        return (sub)


