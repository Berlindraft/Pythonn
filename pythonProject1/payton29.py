# STACK
# ZYRON

class Stack:
    def __init__(self):
        """
        Initialize an empty stack.
        """
        self.items = []

    def is_empty(self):
        """
        Check if the stack is empty.
        :return: True if stack is empty, False otherwise.
        """
        return len(self.items) == 0

    def push(self, item):
        """
        Push an item onto the stack.
        :param item: Item to be pushed onto the stack.
        """
        self.items.append(item)

    def pop(self):
        """
        Remove and return the top item from the stack.
        :return: The top item from the stack.
        """
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("Pop from an empty stack")

    def peek(self):
        """
        Return the top item from the stack without removing it.
        :return: The top item from the stack.
        """
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("Peek from an empty stack")

    def size(self):
        """
        Return the number of items in the stack.
        :return: Number of items in the stack.
        """
        return len(self.items)

# Example usage:
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)

print("Stack size:", stack.size())  # Output: Stack size: 3
print("Top item:", stack.peek())    # Output: Top item: 3

print("Popped item:", stack.pop())  # Output: Popped item: 3
print("Stack size after pop:", stack.size())  # Output: Stack size after pop: 2

print("Is stack empty?", stack.is_empty())  # Output: Is stack empty? False

