# BINARY SEARCH TREE
# ZYRON
class Node:
    def __init__(self, key):
        """
        Initialize a node with a key, and pointers to left and right children.
        """
        self.key = key
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        """
        Initialize an empty binary search tree.
        """
        self.root = None

    def insert(self, key):
        """
        Insert a key into the binary search tree.
        """
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert(self.root, key)

    def _insert(self, current_node, key):
        if key < current_node.key:
            if current_node.left is None:
                current_node.left = Node(key)
            else:
                self._insert(current_node.left, key)
        elif key > current_node.key:
            if current_node.right is None:
                current_node.right = Node(key)
            else:
                self._insert(current_node.right, key)

    def search(self, key):
        """
        Search for a key in the binary search tree.
        Returns True if the key is found, False otherwise.
        """
        return self._search(self.root, key)

    def _search(self, current_node, key):
        if current_node is None:
            return False
        if key == current_node.key:
            return True
        elif key < current_node.key:
            return self._search(current_node.left, key)
        else:
            return self._search(current_node.right, key)

    def delete(self, key):
        """
        Delete a key from the binary search tree.
        """
        self.root = self._delete(self.root, key)

    def _delete(self, current_node, key):
        if current_node is None:
            return current_node

        # Find the node to be deleted
        if key < current_node.key:
            current_node.left = self._delete(current_node.left, key)
        elif key > current_node.key:
            current_node.right = self._delete(current_node.right, key)
        else:
            # Node with only one child or no child
            if current_node.left is None:
                return current_node.right
            elif current_node.right is None:
                return current_node.left

            # Node with two children: Get the inorder successor
            temp = self._min_value_node(current_node.right)
            current_node.key = temp.key
            current_node.right = self._delete(current_node.right, temp.key)

        return current_node

    def _min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def inorder_traversal(self):
        """
        Perform an in-order traversal of the binary search tree.
        """
        result = []
        self._inorder_traversal(self.root, result)
        return result

    def _inorder_traversal(self, current_node, result):
        if current_node is not None:
            self._inorder_traversal(current_node.left, result)
            result.append(current_node.key)
            self._inorder_traversal(current_node.right, result)


# Example usage:
bst = BinarySearchTree()
bst.insert(50)
bst.insert(30)
bst.insert(20)
bst.insert(40)
bst.insert(70)
bst.insert(60)
bst.insert(80)

print("Inorder traversal of the BST:", bst.inorder_traversal())

# Search for a value
print("Search for 40:", bst.search(40))  # Output: True
print("Search for 100:", bst.search(100))  # Output: False

# Delete a value
bst.delete(20)
print("Inorder traversal after deleting 20:", bst.inorder_traversal())
