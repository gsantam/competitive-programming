from collections import deque
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        vertical_nodes = {}
        queue = deque()
        queue.append([root,0,0])
        while len(queue)>0:
            element,column,depth = queue.popleft()
            if element is None:
                continue
            if column not in vertical_nodes:
                vertical_nodes[column] = []
            vertical_nodes[column].append([depth,element.val])
            queue.append([element.left,column-1,depth+1])
            queue.append([element.right,column+1,depth+1])
        vertical_nodes = {i:sorted(vertical_nodes[i]) for i in vertical_nodes}
        return [[x[1] for x in vertical_nodes[i]] for i in range(min(list(vertical_nodes.keys())),max(list(vertical_nodes.keys()))+1)]

