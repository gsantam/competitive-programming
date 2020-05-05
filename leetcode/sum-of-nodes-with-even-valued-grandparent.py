# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        if root is None:
            return 0
        stack = [(root,None,None)]
        total_sum = 0
        while len(stack) > 0:
            element, parent, grandparent = stack.pop()
            if grandparent is not None and grandparent.val % 2 == 0:
                total_sum+=element.val
            if element.left is not None:
                stack.append((element.left,element,parent))
            if element.right is not None:
                stack.append((element.right,element,parent))
                
        return total_sum

        
