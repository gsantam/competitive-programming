"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""
"""
left and right pointers as synonymous to the predecessor and successor 
"""
class Solution:
    def helper(self,node):
        if node.left is None and node.right is None:
            return node,node
        min_left = node
        max_left = node
        min_right = node
        max_right = node
        if node.left is not None:
            min_left,max_left = self.helper(node.left)
        if node.right is not None:
            min_right,max_right = self.helper(node.right)
            
        if max_left.val!=node.val:
            node.left = max_left
            max_left.right = node
        if min_right.val!=node.val:
            node.right = min_right
            min_right.left = node
            
        return min_left,max_right

        
    
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if root is None:
            return None
        min_, max_ = self.helper(root)
        max_.right = min_
        min_.left = max_
        return min_
        
