class Solution:
    def swap(self,node, father):
        if node is None:
            return None
        if node.next is None:
            return node
        next_node = node.next
        next_next_node = node.next.next
        next_node.next = node
        if father is not None:
            father.next = next_node
        node.next = next_next_node
        self.swap(node.next,node)
        return next_node


    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.swap(head, None)
