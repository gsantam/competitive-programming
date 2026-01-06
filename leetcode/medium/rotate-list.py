class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> 
Optional[ListNode]:
        if not head:
            return None
        l = 0
        or_head = head
        while head is not None:
            l+=1
            head = head.next
        pos = l-k%l
        node = or_head
        for i in range(pos-1):
            node = node.next
        last = or_head
        while last.next is not None:
            last = last.next
        last.next = or_head
        new_head = node.next
        node.next = None
        return new_head
