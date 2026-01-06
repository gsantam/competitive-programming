from collections import deque
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        queue = deque()
        queue.append([root,0,0])
        prev_depth = -1
        prev_pos=(2**(0-1)-1)
        while len(queue)!=0:
            node, depth, pos = queue.popleft()
            if node is None:
                continue
            if pos == 0:
                if not (prev_pos==(2**(depth-1)-1) and prev_depth == depth-1):
                    return False
            else:
                if not (prev_pos==pos-1 and prev_depth==depth):
                    return False
            queue.append((node.left,depth+1,2*pos))
            queue.append((node.right,depth+1,2*pos+1))
            prev_pos = pos
            prev_depth = depth
        return True
