class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if head==None:
            return(None)
        if head.next==None and n==1:
            head=None
            return(head)
        else:
            c=head
            count=0
            while head!=None:
                count+=1
                head=head.next
            head=c
            if head.next!=None and count==n:
                head=head.next
                del c
                return(head)
            i=1
            while i!=count-n:
                head=head.next
                i+=1
            t=head.next
            head.next=(head.next).next
            del t
            return(c)