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
        self.__head = None

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

    def search(self, key):
        current = self.__head
        while current:
            if current.data == key:
                return True
            current = current.next
        return False

    def count(self):
        count = 0
        current = self.__head
        while current:
            count += 1
            current = current.next
        return count

    def get_average(self):
        if not self.__head:
            return 0  # Return 0 or None if the list is empty

        total = 0
        count = 0
        current = self.__head

        while current:
            total += current.data  # Add the current node's data to total
            count += 1  # Increment the count of nodes
            current = current.next  # Move to the next node

        return total / count if count > 0 else 0  # Return the average
    def get_max(self):
        if not self.__head:
            return None  # or raise an exception if preferred
        max_value = self.__head.data
        current = self.__head.next
        while current:
            if current.data > max_value:
                max_value = current.data
            current = current.next
        return max_value

    def get_min(self):
        if not self.__head:
            return None  # or raise an exception if preferred
        min_value = self.__head.data
        current = self.__head.next
        while current:
            if current.data < min_value:
                min_value = current.data
            current = current.next
        return min_value

    def is_empty(self):
        return self.__head is None

    def concatenate(self, other):
        if not self.__head:
            self.__head = other.__head
            return
        last = self.__head
        while last.next:
            last = last.next
        last.next = other.__head

    def rotate(self, k):
        if not self.__head or k <= 0:
            return
        # Find the length of the list
        length = 1
        last = self.__head
        while last.next:
            last = last.next
            length += 1

        k = k % length  # In case k is greater than length
        if k == 0:
            return

        # Find the node just before the point of rotation
        current = self.__head
        for _ in range(length - k - 1):
            current = current.next

        new_head = current.next
        current.next = None  # Break the list
        last.next = self.__head  # Link the end to the original head
        self.__head = new_head  # Update head to new head

    def nth_from_start(self, n):
        current = self.__head
        count = 1
        while current and count < n:
            current = current.next
            count += 1
        return current.data if current else None

    def to_list(self):
        result = []
        current = self.__head
        while current:
            result.append(current.data)
            current = current.next
        return result

    def reverse(self):
        prev = None
        current = self.__head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.__head = prev

    def get_middle(self):
        slow = self.__head
        fast = self.__head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow.data if slow else None

    def has_cycle(self):
        slow = fast = self.__head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

    def merge_sorted(self, other):
        dummy = Node(0)
        tail = dummy
        current1 = self.__head
        current2 = other.__head

        while current1 and current2:
            if current1.data < current2.data:
                tail.next = current1
                current1 = current1.next
            else:
                tail.next = current2
                current2 = current2.next
            tail = tail.next

        tail.next = current1 if current1 else current2
        self.__head = dummy.next

    def clear(self):
        self.__head = None

    def remove_duplicates(self):
        current = self.__head
        seen = set()
        previous = None

        while current:
            if current.data in seen:
                previous.next = current.next
            else:
                seen.add(current.data)
                previous = current
            current = current.next

    def get_nth_from_end(self, n):
        length = self.count()
        if n > length:
            return None

        current = self.__head
        for _ in range(length - n):
            current = current.next
        return current.data if current else None

    def split(self):
        if not self.__head or not self.__head.next:
            return self.__head, None

        slow = fast = self.__head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        second_half = slow.next
        slow.next = None  # Terminate the first half
        return self.__head, second_half

    def copy(self):
        if not self.__head:
            return None

        new_list = SinglyLinkedList()
        current = self.__head
        while current:
            new_list.insert_at_end(current.data)
            current = current.next
        return new_list

    def print_reverse(self):
        def _print_reverse(node):
            if node:
                _print_reverse(node.next)
                print(node.data, end=" -> ")

        _print_reverse(self.__head)
        print("wala na finish na haha")
