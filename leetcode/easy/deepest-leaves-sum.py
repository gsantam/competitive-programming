# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def depth_helper(self,deep,node):
        if node is None:
            return deep
        
        if node.left is None and node.right is None:
            if deep not in self.depth_dict:
                self.depth_dict[deep] = 0
            self.depth_dict[deep]+=node.val
            
        self.depth_helper(deep+1,node.left)
        self.depth_helper(deep+1,node.right)
                
            
    def deepestLeavesSum(self, root: TreeNode) -> int:
        self.depth_dict = dict()
        self.depth_helper(0,root)
        max_depth =0
        for depth in self.depth_dict:
            if depth>max_depth:
                max_depth = depth
                sum = self.depth_dict[depth]

        return sum
        
        
