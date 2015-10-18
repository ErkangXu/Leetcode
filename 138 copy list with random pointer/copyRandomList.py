# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    def helper(self, head, i, n2i, i2i, i2n):
        if not head:
            return None
        n2i[head]=i # Set the n2i on the dive-in
        ne=self.helper(head.next,i+1,n2i,i2i,i2n)
        ch=RandomListNode(head.label)
        i2n[i]=ch
        i2i[i]=n2i[head.random] if head.random else -1 # Get n2i and i2i in one pass
        ch.next=ne
        return ch
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        node2index={}
        index2index={}
        index2node={}
        ch=self.helper(head,0,node2index,index2index,index2node)
        for p,q in index2index.iteritems():
            index2node[p].random=None if q==-1 else index2node[q]
        return ch