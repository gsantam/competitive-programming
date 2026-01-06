
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return head
        node = head
        prev = None
        while node is not None:
            copy_node = Node(node.val)
            copy_node.next = None
            if prev is not None:
                prev.next = copy_node
            node.pair = copy_node
            node = node.next
            prev = copy_node
        copy_head = head.pair
        node = head
        while node is not None:
            if node.random is not None:
                pair = node.pair
                random_pair = node.random.pair
                pair.random = random_pair
            else:
                node.pair.random = None
            node = node.next
        return copy_head
