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
            
    def appendNodes(self,data_list):
        for data in data_list:
            self.appendNode(data)

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
            
    def print_list(self):
        if self.head is None:
            return
        else:
            actual_node = self.head
            while actual_node is not None:
                print(actual_node.data,end = " ")
                actual_node = actual_node.next
      
"""
x = 5
6 -> 2 -> 3 -> 2 => 6 -> 2 -> 3 -> 2 -> 6 => 2 -> 3 -> 2 -> 6


"""
            
def sum_ll(ll1,ll2):
    n1 = ll1.head
    n2 = ll2.head
    end = False
    rest = 0
    while n1 is not None:
        if not end:
            actual_sum = n1.data + n2.data + rest
        else:
            actual_sum = n1.data + rest
            
        n1.data = actual_sum % 10
        rest = actual_sum // 10
        if not end:
            if n1.next is None or n2.next is None:
                end = True
                if n1.next is None:
                    n1.next = n2.next
                    n2.next = None
            else:
                n2 = n2.next
        last = n1
        n1 = n1.next
        
    if rest!=0:
        node = Node(rest)
        last.next = node

    return ll1
    

