class Node:
    def __init__(self, data):
        self.__data = data
        self.__next = None

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        self.__data = data

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, value):
        self.__next = value


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_beginning(self, data):
        new_node = Node(data)  # Step 1: Create a new node with the given data

        # Step 2: Check if the list is non-empty
        if self.head:
            new_node.next = self.head  # Link new_node to the current head
            self.head = new_node  # Update head to the new node
        else:
            self.head = new_node  # If empty, set new_node as the head

    def insert_at_end(self, data):
        new_node = Node(data)  # Step 1: Create a new node with the given data

        # Step 2: Check if the list is empty
        if not self.head:
            self.head = new_node  # If empty, make new_node the head
            return

        # Step 3: Traverse to the last node
        last = self.head  # Start from the head
        while last.next:  # Move to the next node until the end is reached
            last = last.next

        # Step 4: Link the new node at the end
        last.next = new_node  # Set the `next` of the last node to new_node

    def insert_before(self, key, value):
        assert self.head, 'Linked list is empty'

        node = Node(value)  # Create a new node with the given value
        current = self.head  # Start from the head of the list
        pre_current = None  # Variable to track the node before `current`

        # Traverse the list to find the node with `key`
        while current.data != key:
            pre_current = current
            current = current.next

        # Insert `node` before `current`
        pre_current.next = node
        node.next = current

    def insert_after(self, key, value):
        assert self.head, 'Linked list is empty'

        # Start from the head of the list
        current = self.head

        # Traverse to find the node with `key`
        while current and current.data != key:
            current = current.next

        # If key is not found in the list
        if not current:
            print(f"Node with data {key} not found.")
            return

        # Create a new node and insert it after `current`
        new_node = Node(value)
        new_node.next = current.next
        current.next = new_node

    # Traversing
    def display(self):
        current = self.head
        assert self.head, 'linked list is empty'
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("wala na finish na haha")

    # Deletions
    def delete_first(self):
        assert self.head, 'list is empty'
        self.head = self.head.next

    def delete_last(self):
        assert self.head, 'list is empty'

        if not self.head.next:  # Only one node in the list
            self.head = None
            return

        current = self.head
        # while current.next and current.next.next:
        #     current = current.next
        # current.next = None

        while current.next:
            pre_current = current
            current = current.next
        pre_current.next = None

    def delete_node(self, target_data):
        # Ensure the list is not empty
        assert self.head, 'list is empty'

        # If the node to be deleted is the head
        if self.head.data == target_data:
            # Update head to the next node
            self.head = self.head.next
            return  # Exit the method

        current = self.head  # Start at the head of the list

        # Traverse the list to find the target node
        while current.next and current.next.data != target_data:
            current = current.next  # Move to the next node

        # If we reached the end and did not find the target node
        if not current.next:
            print("Node with data", target_data, "not found.")  # Inform the user
            return  # Exit the method

        # Delete the target node by linking to the next node
        current.next = current.next.next

