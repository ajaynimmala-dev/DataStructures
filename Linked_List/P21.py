
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        value2 =None
        if list1==None and list2==None:
            return(None)
        if list1==None:
            return(list2)
        if list2==None:
            return list1
        else:
            i=1
            while list1!=None and list2!=None:
                if list1.val<list2.val:
                    value=list1.val
                    list1=list1.next
                else:
                    if list1.val>list2.val:
                        value=list2.val
                        list2=list2.nex
                    else:
                        value=list1.val
                        value2=list2.val
                        list1=list1.next
                        list2=list2.next
                c=ListNode()
                if i==1 and value2!=None:
                    h=c
                    l=c
                    l.val=value
                    c=ListNode()
                    l.next=c
                    l=c
                    l.val=value2
                    i=i+1
                    value2=None
                else:
                    if i==1 and value2==None:
                        h=c
                        l=c
                        l.val=value
                        i+=1
                    else:
                        if value2==None:
                            l.next=c
                            l=c
                            l.val=value
                        else:
                            l.next=c
                            l=c
                            l.val=value
                            c=ListNode()
                            l.next=c
                            l=c
                            l.val=value2
                            value2=None
            if list1:
                l.next=list1
                return(h)
            elif list2:
                l.next=list2
                return(h)
            else:
                return(h)





