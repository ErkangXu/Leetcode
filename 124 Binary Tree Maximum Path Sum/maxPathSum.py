# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    maxS=0 # Need to give a value to define it
    def helper(self,root):
        if not root:
            return 0
        left=self.helper(root.left)
        right=self.helper(root.right)
        m=root.val
        if left>0: 
            m+=left
        if right>0:
            m+=right
        if m>self.maxS:
            self.maxS=m
        r=root.val
        if max(left,right)>0:
            r+=max(left,right)
        return r
        
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.maxS=root.val
        self.helper(root)
        return self.maxS