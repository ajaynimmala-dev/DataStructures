class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        c=head
        if c==None:
            return(None)
        else:
            res=[]
            while c!=None:
                res.append(c.val)
                c=c.next
            c=head
            del head
            del c
            res=[x for x in res if res.count(x)==1]
            h=None
            for i in res:
                c=ListNode()
                if res.index(i)==0:
                    h=c
                    l=c
                    l.val=i
                else:
                    l.next=c
                    l=c
                    l.val=i
                    del c
            return(h)