# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def helper(self,lists):
        print("In helper")
        print("list is")
        print(lists)
        print
        length=len(lists)
        if length==1:
            return lists[0]
        elif length==2:
            dummyHead=ListNode(0)
            pn=dummyHead
            while lists[0] and lists[1]:
                if lists[0].val<lists[1].val:
                    pn.next=lists[0]
                    lists[0]=lists[0].next
                else:
                    pn.next=lists[1]
                    lists[1]=lists[1].next
                pn=pn.next
            if not lists[0]:
                pn.next=lists[1]
            else:
                pn.next=lists[0]
            return dummyHead.next
        else:
            return self.helper( [self.helper(lists[:length/2]), self.helper(lists[length/2:])] ) #Forgot to return at first
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        noneIndexList=[]
        for i in xrange(len(lists)):
            if not lists[i]:
                noneIndexList.append(i)
        offset=0
        for i in noneIndexList:
            lists.pop(i-offset)
            offset+=1
        if not lists:
            return None
        return self.helper(lists)
