# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        queue = []

        def enqueue(r):
            if r == None:
                return r
            else:
                queue.append(r)

        def dequeue():
            if len(queue) == 0:
                return None
            else:
                return queue.pop(0)

        def bfs(r):
            if r == None or len(queue) == 0:
                return
            else:
                temp = []
                l = len(queue)
                for _ in range(l):
                    r = dequeue()
                    temp.append(r.val)
                    enqueue(r.left)
                    enqueue(r.right)
                res.append(temp.copy())
                bfs(r)

        enqueue(root)
        bfs(root)
        res.reverse()
        return res

