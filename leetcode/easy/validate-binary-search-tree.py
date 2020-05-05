# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution():

    def validate(self,node):
        max_val = node.val
        min_val = node.val
        if node.left is None and node.right is None:
            return max_val,min_val,True
        if node.left is not None:
            max_val_left,min_val_left,is_valid = self.validate(node.left)
            min_val = min_val_left
            if is_valid == False or max_val_left>=node.val:
                return 0,0,False
        if node.right is not None:
            max_val_right,min_val_right,is_valid = self.validate(node.right)
            max_val = max_val_right
            if is_valid == False or min_val_right<=node.val:
                return 0,0,False
        
        return max_val,min_val,True
            
    
    def isValidBST(self, root: TreeNode) -> bool:
        if root is None:
            return True
        max_val,min_val,valid = self.validate(root)
        return valid

        
