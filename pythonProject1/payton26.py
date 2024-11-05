# CIRCULAR LINKED LIST
# ZYRON

class Node:
    def __init__(self, data=None):
        self.data = data  # Stores the data of the node
        self.next = None  # Pointer to the next node

class CircularLinkedList:
    def __init__(self):
        self.head = None  # Initialize the head of the list as None

    def append(self, data):
        """
        Insert a new node at the end of the circular linked list.
        """
        new_node = Node(data)
        if self.head is None:  # If the list is empty
            self.head = new_node
            self.head.next = self.head  # Point to itself
        else:
            current_node = self.head
            while current_node.next != self.head:  # Traverse to the last node
                current_node = current_node.next
            current_node.next = new_node
            new_node.next = self.head  # Link the new node to head

    def prepend(self, data):
        """
        Insert a new node at the beginning of the circular linked list.
        """
        new_node = Node(data)
        if self.head is None:  # If the list is empty
            self.head = new_node
            self.head.next = self.head  # Point to itself
        else:
            new_node.next = self.head
            current_node = self.head
            while current_node.next != self.head:  # Traverse to the last node
                current_node = current_node.next
            current_node.next = new_node
            self.head = new_node  # Update the head to the new node

    def delete_node(self, key):
        """
        Delete the first occurrence of a node with the given data.
        """
        if self.head is None:
            return

        current_node = self.head
        prev_node = None

        # Case when the node to be deleted is the head node
        if current_node.data == key:
            if current_node.next == self.head:  # Only one node in the list
                self.head = None
            else:
                while current_node.next != self.head:  # Find the last node
                    current_node = current_node.next
                current_node.next = self.head.next
                self.head = self.head.next
            return

        prev_node = self.head
        current_node = self.head.next

        while current_node != self.head:
            if current_node.data == key:
                prev_node.next = current_node.next
                return
            prev_node = current_node
            current_node = current_node.next

    def display(self):
        """
        Display the entire circular linked list.
        """
        nodes = []
        current_node = self.head
        if self.head is not None:
            while True:
                nodes.append(str(current_node.data))
                current_node = current_node.next
                if current_node == self.head:
                    break
        print(" -> ".join(nodes) + " -> (head)")

# Example usage:
cll = CircularLinkedList()
cll.append(1)
cll.append(2)
cll.append(3)
cll.prepend(0)
cll.display()  # Output: 0 -> 1 -> 2 -> 3 -> (head)
cll.delete_node(2)
cll.display()  # Output: 0 -> 1 -> 3 -> (head)
