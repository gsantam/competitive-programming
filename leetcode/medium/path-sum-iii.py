from collections import defaultdict
class Solution:
    def sum_children(self,node,targetSum):
        if node is None:
            return {}
        n_left = self.sum_children(node.left,targetSum)
        n_right = self.sum_children(node.right,targetSum)
        n_node = defaultdict(lambda:0)
        for sum_ in n_left:
            n_node[sum_+node.val]+=n_left[sum_]
        for sum_ in n_right:
            n_node[sum_+node.val]+=n_right[sum_]
        n_node[node.val]+=1
        self.total_sum+=n_node[targetSum]  
        return  n_node


    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.total_sum = 0
        self.sum_children(root,targetSum)
        return self.total_sum
