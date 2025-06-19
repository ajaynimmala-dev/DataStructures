# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = []
        res = []
        if root == None:
            return []
        else:
            def enqueue(r):
                if r == None:
                    return
                else:
                    queue.append(r)

            def dequeue():
                if len(queue) == 0:
                    return None
                else:
                    return queue.pop(0)

            def bfs(root):
                if root == None or len(queue) == 0:
                    return
                else:
                    temp = []
                    l = len(queue)
                    for _ in range(l):
                        root = dequeue()
                        temp.append(root.val)
                        enqueue(root.left)
                        enqueue(root.right)
                    res.append(temp.copy())
                    bfs(root)

            enqueue(root)
            bfs(root)
            return res














