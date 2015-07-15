# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer[]}
    def preorderTraversal(self, root):
        result=[]
        if not root:
            return []
        stack=[]
        stack.append(root)
        while stack:
            holder=stack.pop()
            while 1:
                result.append(holder.val)
                if holder.right:
                    stack.append(holder.right)
                if not holder.left:
                    break
                holder=holder.left
        return result