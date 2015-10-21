# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack=[]
        result=[]
        while root:
            stack.append(root)
            root=root.left
        lastNode=None
        while stack:
            ptr=stack[-1].right
            if not ptr or ptr is lastNode:
                lastNode=stack.pop()
                result.append(lastNode.val)
                continue
            while ptr:
                stack.append(ptr)
                ptr=ptr.left
        return result