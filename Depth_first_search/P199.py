# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue=[]
        main=[]
        def dfs(queue,main):
            if not len(queue):
                return
            else:
                l=len(queue)
                main.append(queue[-1].val)
                for i in range(l):
                    r=queue.pop(0)
                    if r.left:
                        queue.append(r.left)
                    if r.right:
                        queue.append(r.right)
                dfs(queue,main)
        if not root:
            return []
        else:
            queue.append(root)
            dfs(queue,main)
            return main
