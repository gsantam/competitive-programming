class Node():
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = None

    def appendNode(self,data):
        node = Node(data)
        if self.head == None:
            self.head = node

        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = node

    def prependNode(self,data):
        node = Node(data)
        node.next = self.head
        self.head = node

    def deleteWithValue(self,data):
        if self.head == None:
            return

        if self.head.data == data:
            self.head = self.head.next
            return

        current_node = self.head
        while current_node.next is not None:
            if current_node.next.data == data:
                current_node.next = current_node.next.next
                return
            current_node = current_node.next
            
            
            
def remove_duplicate_next(node,seen_values):
    if node is not None:
        if node.next is not None:
            if node.next.data in seen_values:
                node.next = node.next.next
            else:
                seen_values.add(node.next.data)
                
            remove_duplicate_next(node.next,seen_values)
    
            
            
def remove_duplicates(linked_list):
    if linked_list is None:
        return
    seen_values = set()
    if linked_list.head is not None:
        seen_values.add(linked_list.head.data)
        remove_duplicate_next(linked_list.head,seen_values)
    
    
