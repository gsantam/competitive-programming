# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def helper(self,node,target):
        if abs(node.val-target) < abs(self.min_difference-target):
            self.min_difference = node.val
        if node.left is not None:
            self.helper(node.left,target)
        if node.right is not None:
            self.helper(node.right,target)
    def closestValue(self, root: TreeNode, target: float) -> int:
        self.min_difference = 10**10
        self.helper(root,target)
        
        return self.min_difference
