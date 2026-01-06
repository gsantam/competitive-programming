class Solution:
    def check_depth_balance(self,node):
        if node is None:
            return True, -1
        left_depth,left_balance = self.check_depth_balance(node.left)
        right_depth,right_balance = self.check_depth_balance(node.right)
        balance_diff = abs(left_depth-right_depth)
        is_balance = left_balance and right_balance and balance_diff<=1
        return max(left_depth,right_depth)+1, is_balance

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        depth,balance = self.check_depth_balance(root)
        return balance
