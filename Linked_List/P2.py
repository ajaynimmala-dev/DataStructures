class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        res1=[]
        res2=[]
        while (l1!=None or l2!=None):
            if l1!=None:
                res1.append(l1.val)
                l1=l1.next
            if l2!=None:
                res2.append(l2.val)
                l2=l2.next
        res1.reverse()
        res2.reverse()
        sum1=0
        sum2=0
        for i in res1:
            sum1=sum1*10+i
        for i in res2:
            sum2=sum2*10+i
        sum1=sum1+sum2
        if sum1==0:
            h=ListNode()
            return(h)
        else:
            res=[]
            while sum1!=0:
                res.append(sum1%10)
                sum1=sum1/10
        for i in range(len(res)):
            if i==0:
                h=ListNode()
                h.val=res[i]
                l=h
            else:
                c=ListNode()
                l.next=c
                l=c
                l.val=res[i]
        return(h)