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
    def connect(self, root: 'Node') -> 'Node':
        queue = []

        def solve(queue):
            if not len(queue):
                return
            else:
                l = len(queue)
                for i in range(l):
                    r = queue.pop(0)
                    if i != l - 1:
                        r.next = queue[0]
                    else:
                        r.next = None
                    if r.left:
                        queue.append(r.left)
                    if r.right:
                        queue.append(r.right)
                solve(queue)

        if root == None:
            return None
        else:
            queue.append(root)
            solve(queue)
            return root

66