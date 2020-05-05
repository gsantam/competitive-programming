# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def helper(self,node,depth):
        if depth not in self.nodes:
            self.nodes[depth] = node.val
            
        if node.right is not None:
            self.helper(node.right,depth+1)
        if node.left is not None:
            self.helper(node.left,depth+1)
        return
    def rightSideView(self, root: TreeNode) -> List[int]:
        self.nodes = {}
        if root is None:
            return []
        
        self.helper(root,0)
        nodes = [self.nodes[depth] for depth in self.nodes]
        return nodes
        
