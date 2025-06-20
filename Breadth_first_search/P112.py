# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(r,targetSum):
            if not r:
                return False
            else:
                if not r.left and not r.right:
                    return targetSum==r.val
                else:
                    left=dfs(r.left,targetSum-r.val)
                    right=dfs(r.right,targetSum-r.val)
                    return left or right
        return dfs(root,targetSum)
