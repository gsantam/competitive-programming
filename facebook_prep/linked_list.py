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
            
        
        
    
            
    
    
