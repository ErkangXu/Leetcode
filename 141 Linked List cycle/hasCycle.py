# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a boolean
    def hasCycle(self, head):
        if not head:
            return False
        fast=head
        slow=head
        while fast.next and fast.next.next:
            fast=fast.next.next
            slow=slow.next
            if fast is slow:
                return True
        return False