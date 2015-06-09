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
        while pointer is not None:
            holder=pointer.next
            if pointer.val<head.val:
                pointer.next=head
                head=pointer
            else:
                ite=head
                while ite.next is not None and pointer.val>ite.next.val :
                    ite=ite.next
                pointer.next=ite.next
                ite.next=pointer
            pointer=holder
        return head