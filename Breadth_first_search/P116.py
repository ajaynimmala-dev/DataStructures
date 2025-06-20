"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        queue = []

        def bfs(queue):
            if not len(queue):
                return
            else:
                l = len(queue)
                for i in range(len(queue)):
                    r = queue.pop(0)
                    if not r:
                        continue
                    else:
                        if i == l - 1:
                            r.next = None
                        else:
                            r.next = queue[0]
                        queue.append(r.left)
                        queue.append(r.right)
                bfs(queue)

        if not root:
            return None
        else:
            queue.append(root)
            bfs(queue)
            return root





