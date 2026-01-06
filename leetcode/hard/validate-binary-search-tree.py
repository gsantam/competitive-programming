class Solution:
    def valid_recurse(self,node,low,high):
        if node is None:
            return True
        if node.val<=low or node.val>=high:
            return False
        return self.valid_recurse(node.left,low,node.val) and self.valid_recurse(node.right,node.val,high)

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.valid_recurse(root,-10**10,10**10)
