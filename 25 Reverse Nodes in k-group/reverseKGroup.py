# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        nh=ListNode(-1)
        cnt=nh
        stk=[]
        while head:
            i=0
            hk=head
            while head and i<k:
                stk.append(head)
                head=head.next
                i+=1
            if not head and i<k:
                while hk:
                    cnt.next=hk
                    cnt=cnt.next
                    hk=hk.next
            else:
                while stk:
                    cnt.next=stk.pop()
                    cnt=cnt.next
        cnt.next=None
        return nh.next