# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer[][]}
    def zigzagLevelOrder(self, root):
        if root is None:
            return []
        result=[]
        updatingList=[]
        updatingList.append(root)
        indicater=1
        while updatingList:
            valueList=[]
            if indicater==1:
                for n in updatingList:
                    valueList.append(n.val)
            else:
                for n in reversed(updatingList):
                    valueList.append(n.val)
            result.append(valueList)
            newList=[]
            for i in updatingList:
                if i.left is not None:
                    newList.append(i.left)
                if i.right is not None:
                    newList.append(i.right)
            updatingList=newList
            indicater*=-1
        return result