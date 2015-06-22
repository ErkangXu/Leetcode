# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTreeHelper(self, inorder, ist, ien, postorder, pst, pen):
        if(ist>ien):
            return None
        rootV=postorder[pen]
        i=inorder.index(rootV)  # use the buildin index function to find the index reduce the time from 600ms to 120ms
        root = TreeNode(rootV)
        lh=self.buildTreeHelper(inorder,ist,i-1,postorder,pst,pst+i-ist-1)
        rh=self.buildTreeHelper(inorder,i+1,ien,postorder,pst+i-ist,pen-1)
        root.left=lh
        root.right=rh
        return root
                
    # @param {integer[]} inorder
    # @param {integer[]} postorder
    # @return {TreeNode}
    def buildTree(self, inorder, postorder):
        iList=list(inorder) # construct list at the beginning and pass in, not every time in the helper body
        pList=list(postorder)
        return self.buildTreeHelper(iList, 0, len(inorder)-1, pList, 0, len(postorder)-1)