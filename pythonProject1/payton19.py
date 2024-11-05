
# Section: BSIT II-B

# Template for the node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Template for the stack
class Stack:
    def __init__(self):     
        self.top = None

    # Push Method
    def push(self, data):
        node = Node(data)

        if self.top is None:  # if there is no top value it solely assigns the node
            self.top = node
        else:  # otherwise the top data will be pushed and be reassigned by the new node
            node.next = self.top
            self.top = node

    def peek(self):  # this is a method with a TERNARY statement returning the value of top data
        return None if self.top is None else self.top.data

    def pop(self):  # this method returns the value of the top node and removes it from the stack
        if self.top is None:
            print("Stack is empty")
        else:
            x = self.top.data
            self.top = self.top.next  # The TOP VALUE will be reassigned to the next value
            return x  # after the operations it return the value of the removed node

    def is_Balance(self, str):  # This is a special method which checks if the passed string contains paired characters
        for i in str:  # storing the special characters to the stack
            if i == '(' or i == '{' or i == '[':  # condition that it is among the paired characters
                self.push(i)
        for i in str:  # This loop checks the other special character's pair
            if i == ')':
                if self.peek() == '(':  # if the other pair is encountered and the top valuue is its other pair also
                    self.pop()  # it would be popped out from the stack
                else:
                    return False  # else it returns false
            elif i == '}':
                if self.peek() == '{':
                    self.pop()
                else:
                    return False
            elif i == ']':
                if self.peek() == '[':
                    self.pop()
                else:
                    return False

        return True if self.peek() is None else False  # if the top value is None then it returns True else False

    def display(self):
        current = self.top

        if current is None:
            print("Stack is empty...")
        while current is not None:
            print(current.data, end="\n")
            current = current.next


s = Stack()
print("Is Balance:", s.is_Balance('((]))'))
