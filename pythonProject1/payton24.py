# SINGLY LINKED LIST
# ZYRON

class Node:
    def __init__(self, data=None):
        self.data = data  # Stores the data of the node
        self.next = None  # Pointer to the next node

class SinglyLinkedList:
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

    def prepend(self, data):
        """
        Insert a new node at the beginning of the list.
        """
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete_node(self, key):
        """
        Delete the first occurrence of a node with the given data.
        """
        current_node = self.head

        # If the node to be deleted is the head node
        if current_node and current_node.data == key:
            self.head = current_node.next
            current_node = None
            return

        prev_node = None
        while current_node and current_node.data != key:
            prev_node = current_node
            current_node = current_node.next

        if current_node is None:
            print(f"Node with data {key} not found.")
            return

        prev_node.next = current_node.next
        current_node = None

    def display(self):
        """
        Display the entire linked list.
        """
        current_node = self.head
        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("None")

# Example usage:
sll = SinglyLinkedList()
sll.append(1)
sll.append(2)
sll.append(3)
sll.prepend(0)
sll.display()  # Output: 0 -> 1 -> 2 -> 3 -> None
sll.delete_node(2)
sll.display()  # Output: 0 -> 1 -> 3 -> None
