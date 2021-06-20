class Solution:
    def recursion(self,node):
        if node.left is not None:
            left_best = self.recursion(node.left)
        else:
            left_best = [0,0]
        if node.right is not None:
            right_best = self.recursion(node.right)
        else:
            right_best = [0,0]
            
        return [node.val + left_best[1] + right_best[1], max(left_best[0],left_best[1]) + max(right_best[0],right_best[1])]
        
        
        
    def rob(self, root: TreeNode) -> int:
        if root is None:
            return 0
        best_root = self.recursion(root)
        return max(best_root[0],best_root[1])
