# DYNAMIC ARRAYS
# ZYRON

import ctypes

class DynamicArray(object):
    '''
    DYNAMIC ARRAY CLASS (Similar to Python List)
    '''

    def __init__(self):
        self.n = 0  # Count actual elements (Default is 0)
        self.capacity = 1  # Default Capacity
        self.A = self.make_array(self.capacity)

    def __len__(self):
        """
        Return number of elements stored in array
        """
        return self.n

    def __getitem__(self, k):
        """
        Return element at index k
        """
        if not 0 <= k < self.n:
            # Check if k index is in bounds of array
            raise IndexError('K is out of bounds!')

        return self.A[k]  # Retrieve from the array at index k

    def append(self, ele):
        """
        Add element to end of the array
        """
        if self.n == self.capacity:
            # Double capacity if not enough room
            self._resize(2 * self.capacity)

        self.A[self.n] = ele  # Set self.n index to element
        self.n += 1

    def insert_at(self, item, index):
        """
        This function inserts the item at any specified index.
        """
        if index < 0 or index > self.n:
            print("Please enter an appropriate index.")
            return

        if self.n == self.capacity:
            self._resize(2 * self.capacity)

        for i in range(self.n - 1, index - 1, -1):
            self.A[i + 1] = self.A[i]

        self.A[index] = item
        self.n += 1

    def delete(self):
        """
        This function deletes an item from the end of the array
        """
        if self.n == 0:
            print("Array is empty, deletion not possible.")
            return

        self.A[self.n - 1] = 0
        self.n -= 1

    def remove_at(self, index):
        """
        This function deletes an item from a specified index.
        """
        if self.n == 0:
            print("Array is empty, deletion not possible.")
            return

        if index < 0 or index >= self.n:
            raise IndexError("Index out of bounds, deletion not possible.")

        if index == self.n - 1:
            self.A[index] = 0
            self.n -= 1
            return

        for i in range(index, self.n - 1):
            self.A[i] = self.A[i + 1]

        self.A[self.n - 1] = 0
        self.n -= 1

    def _resize(self, new_cap):
        """
        Resize internal array to capacity new_cap
        """
        B = self.make_array(new_cap)  # New bigger array

        for k in range(self.n):  # Reference all existing values
            B[k] = self.A[k]

        self.A = B  # Call A the new bigger array
        self.capacity = new_cap  # Reset the capacity

    def make_array(self, new_cap):
        """
        Returns a new array with new_cap capacity
        """
        return (new_cap * ctypes.py_object)()


# Instantiate the dynamic array
arr = DynamicArray()

# Append new elements
arr.append(1)
arr.append(2)
arr.append(3)

# Get the length of the array
print(len(arr))

# Access elements in the array
print(arr[1])
print(arr[2])

# Remove an element at index 2
arr.remove_at(2)

# Get the length of the array after removal
print(len(arr))

# Access an element after removal
print(arr[1])

# This code was contributed by Raja Ramakrishna
