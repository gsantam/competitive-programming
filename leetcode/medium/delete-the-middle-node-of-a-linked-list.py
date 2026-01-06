class Solution:
    def back_and_forth_list(self,parent,node,length_so_far):
        if node.next is None:
            total_length = length_so_far
        else:
            total_length = self.back_and_forth_list(node,node.next,length_so_far+1)
        if length_so_far==((total_length+1)//2):
            parent.next = node.next
        return total_length


    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next is None:
            return None
        self.back_and_forth_list(None,head,0)
        return head
