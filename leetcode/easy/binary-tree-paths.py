class Solution:
    def recursive_traverse(self,node):
        if node.left is None and node.right is None:
            return [str(node.val)]
        total_paths = []
        if node.left:
            left_paths = self.recursive_traverse(node.left)
            for left_path in left_paths:
                total_paths.append(str(node.val) + "->" + left_path)
        if node.right:
            right_paths = self.recursive_traverse(node.right)
            for right_path in right_paths:
                total_paths.append(str(node.val) + "->" + right_path)
        return total_paths
        
        


    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        return self.recursive_traverse(root)
