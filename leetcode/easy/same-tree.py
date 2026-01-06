class Solution:
    def compare_nodes(self,p,q):
        if p is None and q is None:
            return True
        if (p is None and q is not None) or (p is not None and q is None):
            return False
        if p.val != q.val:
            return False
        return self.compare_nodes(p.left,q.left) and self.compare_nodes(p.right,q.right)
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return self.compare_nodes(p,q)
