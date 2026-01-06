class Solution:
    def depth(self,node):
        if node is None:
            return 0
        return max(self.depth(node.left),self.depth(node.right)) + 1

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.depth(root)
