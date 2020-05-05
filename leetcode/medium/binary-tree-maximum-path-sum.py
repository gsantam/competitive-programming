# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def helper(self,node):
        if node is None:
            return 0
        
        left_value = self.helper(node.left)
        right_value = self.helper(node.right)
        
        best_path = max(node.val, left_value + node.val)
        best_path = max(best_path, right_value + node.val)
        best_path_ = max(best_path, right_value +left_value+  node.val)

        
        self.max_path = max(self.max_path,best_path_)
        
        return best_path
            
        
        
        
    def maxPathSum(self, root: TreeNode) -> int: 
        self.max_path = -10**10
        self.helper(root)
        return self.max_path
        
