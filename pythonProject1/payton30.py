# QUEUE
# ZYRON
class Queue:
    def __init__(self):
        """
        Initialize an empty queue.
        """
        self.items = []

    def is_empty(self):
        """
        Check if the queue is empty.
        :return: True if the queue is empty, False otherwise.
        """
        return len(self.items) == 0

    def enqueue(self, item):
        """
        Add an item to the rear of the queue.
        :param item: Item to be added to the queue.
        """
        self.items.append(item)

    def dequeue(self):
        """
        Remove and return the front item from the queue.
        :return: The front item from the queue.
        """
        if not self.is_empty():
            return self.items.pop(0)
        else:
            raise IndexError("Dequeue from an empty queue")

    def peek(self):
        """
        Return the front item from the queue without removing it.
        :return: The front item from the queue.
        """
        if not self.is_empty():
            return self.items[0]
        else:
            raise IndexError("Peek from an empty queue")

    def size(self):
        """
        Return the number of items in the queue.
        :return: Number of items in the queue.
        """
        return len(self.items)

# Example usage:
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

print("Queue size:", queue.size())  # Output: Queue size: 3
print("Front item:", queue.peek())  # Output: Front item: 1

print("Dequeued item:", queue.dequeue())  # Output: Dequeued item: 1
print("Queue size after dequeue:", queue.size())  # Output: Queue size after dequeue: 2

print("Is queue empty?", queue.is_empty())  # Output: Is queue empty? False

