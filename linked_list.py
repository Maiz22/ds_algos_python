class Node:
    """
    Class representing a node of a linked list.
    """
    def __init__(self, val) -> None:
        self.val = val
        self.next = None

class LinkedList:
    """
    Class representing a linked list.
    """
    def __init__(self) -> None:
        self.head = None

    def append(self, node:Node) -> None:
        """
        Takes a node and adds it to the end of the linked 
        list. 
        """
        if self.head is None:
            self.head = node
        else:
            cur_node = self.head
            while cur_node.next:
                cur_node = cur_node.next
            cur_node.next = node

    def __len__(self) -> int:
        """
        Returning the length of the linked list by overwriting
        the len method.
        """
        count = 0
        cur_node = self.head
        while cur_node:
            count += 1
            cur_node = cur_node.next
        return count
    
    def print_values(self) -> None:
        """
        Prints all the values of the linked list.
        """
        cur_node = self.head
        while cur_node:
            print(cur_node.val)
            cur_node = cur_node.next


if __name__ == "__main__":
    node1 = Node(val=1)
    node2 = Node(val=2)
    node3 = Node(val=3)
    linked_list = LinkedList()
    linked_list.append(node1)
    linked_list.append(node2)
    linked_list.append(node3)
    print(len(linked_list))
    linked_list.print_values()

    
