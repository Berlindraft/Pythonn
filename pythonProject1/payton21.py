#STATIC ARRAY
#RAYMUND ZYRON ABELLA
import array

# Define a static array
# Syntax: array.array(typecode, [initial_values])
# Example: An array of integers
arr = array.array('i', [0] * 5)  # Creates a static array of integers with 5 elements initialized to 0

# Operations on static array
def print_array(arr):
    """Function to print the elements of the array"""
    for i in arr:
        print(i, end=' ')
    print()

def update_element(arr, index, value):
    """Function to update an element at a specific index"""
    if 0 <= index < len(arr):
        arr[index] = value
    else:
        print("Index out of bounds")

def sum_array(arr):
    """Function to return the sum of all elements"""
    return sum(arr)

def find_max(arr):
    """Function to find the maximum element in the array"""
    return max(arr)

# Example usage
print("Initial array:")
print_array(arr)

# Update element at index 2
update_element(arr, 2, 10)

print("Array after updating index 2:")
print_array(arr)

# Get the sum of elements in the array
print("Sum of array elements:", sum_array(arr))

# Find the maximum element in the array
print("Maximum element in the array:", find_max(arr))
