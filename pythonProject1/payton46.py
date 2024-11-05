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
        new_node = Node(data)

        if self.head:
            new_node.next = self.head
            self.head = new_node
        else:
            self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            return

        last = self.head
        while last.next:
            last = last.next

        last.next = new_node

    def insert_before(self, key, value):
        assert self.head, 'Linked list is empty'

        node = Node(value)
        current = self.head
        pre_current = None

        while current.data != key:
            pre_current = current
            current = current.next

        pre_current.next = node
        node.next = current

    def insert_after(self, key, value):
        assert self.head, 'Linked list is empty'

        current = self.head

        while current and current.data != key:
            current = current.next

        if not current:
            print(f"Node with data {key} not found.")
            return

        new_node = Node(value)
        new_node.next = current.next
        current.next = new_node

    def display(self):
        current = self.head
        assert self.head, 'linked list is empty'
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("wala na finish na haha")

    def delete_first(self):
        assert self.head, 'list is empty'
        self.head = self.head.next

    def delete_last(self):
        assert self.head, 'list is empty'

        if not self.head.next:
            self.head = None
            return

        current = self.head
        while current.next:
            pre_current = current
            current = current.next
        pre_current.next = None

    def delete_node(self, target_data):
        assert self.head, 'list is empty'

        if self.head.data == target_data:
            self.head = self.head.next
            return

        current = self.head

        while current.next and current.next.data != target_data:
            current = current.next

        if not current.next:
            print("Node with data", target_data, "not found.")
            return

        current.next = current.next.next

# ======================================================
# ======================================================
# ======================================================
# ======================================================
# ======================================================
# ======================================================
# ======================================================
# ======================================================
# ======================================================

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


class SinglyLinkedListPrivate:
    def __init__(self):
        self.__head = None  # Make head private

    def insert_beginning(self, data):
        new_node = Node(data)

        if self.__head:
            new_node.next = self.__head
            self.__head = new_node
        else:
            self.__head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)

        if not self.__head:
            self.__head = new_node
            return

        last = self.__head
        while last.next:
            last = last.next

        last.next = new_node

    def insert_before(self, key, value):
        assert self.__head, 'Linked list is empty'

        node = Node(value)
        current = self.__head
        pre_current = None

        while current.data != key:
            pre_current = current
            current = current.next

        pre_current.next = node
        node.next = current

    def insert_after(self, key, value):
        assert self.__head, 'Linked list is empty'

        current = self.__head

        while current and current.data != key:
            current = current.next

        if not current:
            print(f"Node with data {key} not found.")
            return

        new_node = Node(value)
        new_node.next = current.next
        current.next = new_node

    def display(self):
        current = self.__head
        assert self.__head, 'linked list is empty'
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("wala na finish na haha")

    def delete_first(self):
        assert self.__head, 'list is empty'
        self.__head = self.__head.next

    def delete_last(self):
        assert self.__head, 'list is empty'

        if not self.__head.next:
            self.__head = None
            return

        current = self.__head
        while current.next:
            pre_current = current
            current = current.next
        pre_current.next = None

    def delete_node(self, target_data):
        assert self.__head, 'list is empty'

        if self.__head.data == target_data:
            self.__head = self.__head.next
            return

        current = self.__head

        while current.next and current.next.data != target_data:
            current = current.next

        if not current.next:
            print("Node with data", target_data, "not found.")
            return

        current.next = current.next.next
