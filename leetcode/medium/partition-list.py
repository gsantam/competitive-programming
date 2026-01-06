class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        current_left_node = None
        current_right_node = None
        right_head = None
        left_head = None
        while head:
            if head.val<x:
                if current_left_node is not None:
                    current_left_node.next = head
                else:
                    left_head = head
                current_left_node = head
            else:
                if current_right_node is not None:
                    current_right_node.next = head
                else:
                    right_head = head
                current_right_node = head
            head = head.next
        if current_left_node is not None:
            current_left_node.next = right_head
        if current_right_node is not None:
            current_right_node.next = None
        if left_head is None:
            return right_head
        return left_head
