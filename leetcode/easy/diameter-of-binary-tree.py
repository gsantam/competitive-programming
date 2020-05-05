# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def helper(self,node):
        if node.left is None and node.right is None:
            return 0
        left_path = 0
        right_path = 0
        if node.left is not None:
            left_path = self.helper(node.left) +1 
        if node.right is not None:
            right_path = self.helper(node.right) +1
            
        self.max_path = max(self.max_path,left_path + right_path)
        
        if left_path>=right_path:
            return left_path
        return right_path
            
            
        
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.max_path = 0
        if root is None:
            return 0
        
        self.helper(root)
        return self.max_path
        
        
        
