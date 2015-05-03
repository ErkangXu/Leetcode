# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @return a list of tree node
    def copyTree(self,o,inc):
        if o==None:
            return None
        l = self.copyTree(o.left,inc)
        r = self.copyTree(o.right,inc)
        head = TreeNode(o.val+inc)
        head.left=l
        head.right=r
        return head
        
    def generateTrees(self, n):
        list=[]
        zeroGroup=[]
        zeroGroup.append(None)
        list.append(zeroGroup);
        oneGroup=[]
        oneGroup.append(TreeNode(1))
        list.append(oneGroup)
        if n==0 or n==1:
            return list[n]
        i=2
        while(i<=n): # This is faster than xrange() loop
            tmp=[]
            for j in xrange(i):
                for k in list[j]:
                    for x in list[i-1-j]:
                        head=TreeNode(j+1)
                        head.left=self.copyTree(k,0)
                        head.right=self.copyTree(x,j+1) # increment every element in the right branch
                        tmp.append(head)
            list.append(tmp)
            i+=1
        return list[n]
