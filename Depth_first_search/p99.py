# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        res = []

        def inorder(r):
            if not r:
                return
            else:
                inorder(r.left)
                res.append(r.val)
                inorder(r.right)

        inorder(root)
        temp = res.copy()
        val1 = 0
        temp.sort()
        val2 = 0
        for i in range(len(temp)):
            if temp[i] == res[i]:
                continue
            else:
                val1 = temp[i]
                val2 = res[i]
                break

        def find(r, val1, val2):
            if not r:
                return
            else:
                find(r.left, val1, val2)
                if r.val == val1:
                    r.val = val2
                elif r.val == val2:
                    r.val = val1
                find(r.right, val1, val2)

        find(root, val1, val2)
        return root

