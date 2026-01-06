class Solution:
    def reverse_node(self,node,father):
        if node is None:
            self.head = father
            return
        node_next = node.next
        node.next = father
        self.reverse_node(node_next,node)
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        self.reverse_node(head,None)
        return self.head
