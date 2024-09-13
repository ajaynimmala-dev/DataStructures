# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        c = head
        if c == None or c.next == None:
            return (c)
        else:
            while c != None and c.next != None:
                t = c.val
                c.val = c.next.val
                c.next.val = t
                c = c.next.next
            return (head)

