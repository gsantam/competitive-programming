def has_cycle(head):
    if head is None:
        return False
    actual_node_1 = head
    actual_node_2 = head
    first = True
    while actual_node_1 is not None and actual_node_2 is not None:
        if first:
            first = False
        else:
            if actual_node_1 == actual_node_2:
                return True
        actual_node_1 = actual_node_1.next
        if actual_node_2.next is not None:
            actual_node_2 = actual_node_2.next.next
        else:
            return False

    return False
