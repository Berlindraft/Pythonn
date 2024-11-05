# DOUBLY LINKED LIST
# ZYRON

class Node:
    def __init__(self, data=None):
        self.data = data  # Stores the data of the node
        self.next = None  # Pointer to the next node
        self.prev = None  # Pointer to the previous node

class DoublyLinkedList:
    def __init__(self):
        self.head = None  # Initialize the head of the list as None

    def append(self, data):
        """
        Insert a new node at the end of the list.
        """
        new_node = Node(data)
        if self.head is None:  # If the list is empty
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:  # Traverse to the last node
            last_node = last_node.next
        last_node.next = new_node
        new_node.prev = last_node

    def prepend(self, data):
        """
        Insert a new node at the beginning of the list.
        """
        new_node = Node(data)
        if self.head is None:  # If the list is empty
            self.head = new_node
            return
        self.head.prev = new_node
        new_node.next = self.head
        self.head = new_node

    def delete_node(self, key):
        """
        Delete the first occurrence of a node with the given data.
        """
        current_node = self.head

        # If the node to be deleted is the head node
        if current_node and current_node.data == key:
            if current_node.next:
                current_node.next.prev = None
            self.head = current_node.next
            current_node = None
            return

        while current_node and current_node.data != key:
            current_node = current_node.next

        if current_node is None:
            print(f"Node with data {key} not found.")
            return

        if current_node.next:  # If it's not the last node
            current_node.next.prev = current_node.prev
        if current_node.prev:
            current_node.prev.next = current_node.next
        current_node = None

    def display_forward(self):
        """
        Display the entire linked list from head to tail.
        """
        current_node = self.head
        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("None")

    def display_backward(self):
        """
        Display the entire linked list from tail to head.
        """
        current_node = self.head
        last_node = None
        while current_node:
            last_node = current_node
            current_node = current_node.next
        while last_node:
            print(last_node.data, end=" -> ")
            last_node = last_node.prev
        print("None")

# Example usage:
dll = DoublyLinkedList()
dll.append(1)
dll.append(2)
dll.append(3)
dll.prepend(0)
dll.display_forward()  # Output: 0 -> 1 -> 2 -> 3 -> None
dll.display_backward()  # Output: 3 -> 2 -> 1 -> 0 -> None
dll.delete_node(2)
dll.display_forward()  # Output: 0 -> 1 -> 3 -> None
