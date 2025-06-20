# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []
        main = []
        if not root:
            return []
        if not root.left and not root.right:
            if root.val == targetSum:
                return [[root.val]]

        def dfs(r, sub, res):
            if not r:
                return
            else:
                sub.append(r.val)
                if not r.left and not r.right:
                    if sum(sub) == targetSum:
                        res.append(sub.copy())
                else:
                    dfs(r.left, sub, res)
                    dfs(r.right, sub, res)
                sub.pop()

        dfs(root, main, res)
        return res




