# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def insertionSortList(self, head):
        if head is None:
            return None
        pointer=head.next
        head.next=None
        lastTime=head
        while pointer is not None:
            holder=pointer.next
            if pointer.val<head.val:
                pointer.next=head
                head=pointer
            else:
                ite=head if pointer.val<lastTime.val else lastTime
                while ite.next is not None and pointer.val>ite.next.val :
                    ite=ite.next
                pointer.next=ite.next
                ite.next=pointer
            lastTime=pointer
            pointer=holder
        return head