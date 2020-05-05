# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def traverse_binary_tree(self,node):
        if node is None:
            return
        left_node = node.left
        right_node = node.right
        
        if self.current_node is None:
            self.current_node = node
        else:
            self.current_node.right = node
            self.current_node.left = None
            self.current_node = node
        if left_node is not None:
            self.traverse_binary_tree(left_node)
        if right_node is not None:
            self.traverse_binary_tree(right_node)
        
    def flatten(self, root: TreeNode) -> None:
        self.current_node = None
        self.traverse_binary_tree(root)
        return root
        """
        Do not return anything, modify root in-place instead.
        """
        
