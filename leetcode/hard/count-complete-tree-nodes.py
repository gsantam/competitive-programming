class Solution:
    def exists(self,node,depth,target_node_id,current_depth,current_node_id):
        if current_depth == depth-1:
            if target_node_id==current_node_id*2:
                return node.left is not None
            return node.right is not None
        if target_node_id<=2*current_node_id*(2**(depth-current_depth-1))+2**(depth-current_depth-1) -1:
            return self.exists(node.left,depth,target_node_id,current_depth+1,current_node_id*2)
        return self.exists(node.right,depth,target_node_id,current_depth+1,current_node_id*2+1)

    def countNodes(self, root: Optional[TreeNode]) -> int:
        depth = -1
        node = root
        if root is None:
            return 0
        while node is not None:
            node = node.left
            depth+=1
        if depth == 0:
            return 1
        left = 0
        right = 2**depth-1
        while right - left > 1:
            mid = (left+right)//2
            exists_mid = self.exists(root,depth,mid,0,0)
            if exists_mid:
                left = mid
            else:
                right = mid
        if self.exists(root,depth,right,0,0):
            return 2**depth + right
        return 2**depth + left
