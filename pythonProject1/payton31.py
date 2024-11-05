# DOUBLE ENDED QUEUE
# ZYRON

from collections import deque

class Deque:
    def __init__(self):
        """
        Initialize an empty double-ended queue.
        """
        self.items = deque()

    def is_empty(self):
        """
        Check if the deque is empty.
        :return: True if the deque is empty, False otherwise.
        """
        return len(self.items) == 0

    def add_front(self, item):
        """
        Add an item to the front of the deque.
        :param item: Item to be added to the front of the deque.
        """
        self.items.appendleft(item)

    def add_rear(self, item):
        """
        Add an item to the rear of the deque.
        :param item: Item to be added to the rear of the deque.
        """
        self.items.append(item)

    def remove_front(self):
        """
        Remove and return the front item from the deque.
        :return: The front item from the deque.
        """
        if not self.is_empty():
            return self.items.popleft()
        else:
            raise IndexError("Remove from an empty deque")

    def remove_rear(self):
        """
        Remove and return the rear item from the deque.
        :return: The rear item from the deque.
        """
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("Remove from an empty deque")

    def peek_front(self):
        """
        Return the front item from the deque without removing it.
        :return: The front item from the deque.
        """
        if not self.is_empty():
            return self.items[0]
        else:
            raise IndexError("Peek from an empty deque")

    def peek_rear(self):
        """
        Return the rear item from the deque without removing it.
        :return: The rear item from the deque.
        """
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("Peek from an empty deque")

    def size(self):
        """
        Return the number of items in the deque.
        :return: Number of items in the deque.
        """
        return len(self.items)

# Example usage:
deque = Deque()
deque.add_rear(1)
deque.add_rear(2)
deque.add_front(0)
deque.add_rear(3)

print("Deque size:", deque.size())  # Output: Deque size: 4
print("Front item:", deque.peek_front())  # Output: Front item: 0
print("Rear item:", deque.peek_rear())    # Output: Rear item: 3

print("Removed from front:", deque.remove_front())  # Output: Removed from front: 0
print("Removed from rear:", deque.remove_rear())    # Output: Removed from rear: 3
print("Deque size after removals:", deque.size())  # Output: Deque size after removals: 2

print("Is deque empty?", deque.is_empty())  # Output: Is deque empty? False
