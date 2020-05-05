# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def helper(self, node):
        if node is None:
            return 0,0

        left_value = 0
        left_child_sum = 0
        right_value = 0
        right_child_sum = 0

        if node.left is not None:
            left_value, left_child_sum = self.helper(node.left)

        if node.right is not None:
            right_value, right_child_sum = self.helper(node.right)
            
        best_value = max(node.val + left_child_sum+right_child_sum, left_value+right_value)

        return best_value, left_value + right_value
    
    def rob(self, root: TreeNode) -> int:
        max_value, max_child = self.helper(root)
        return max_value
        
