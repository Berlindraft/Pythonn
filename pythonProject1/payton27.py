def binary_search_iterative(arr, target):
    """
    Perform binary search on a sorted array iteratively.

    :param arr: List of sorted elements
    :param target: Element to search for
    :return: Index of target if found, otherwise -1
    """
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        # Check if target is at mid
        if arr[mid] == target:
            return mid

        # If target is greater, ignore left half
        elif arr[mid] < target:
            left = mid + 1

        # If target is smaller, ignore right half
        else:
            right = mid - 1

    # Target was not found in array
    return -1


# Example usage
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 7
result = binary_search_iterative(arr, target)

if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found in array")


def binary_search_recursive(arr, target, left, right):
    """
    Perform binary search on a sorted array recursively.

    :param arr: List of sorted elements
    :param target: Element to search for
    :param left: Starting index of the search interval
    :param right: Ending index of the search interval
    :return: Index of target if found, otherwise -1
    """
    if left > right:
        return -1  # Base case: target not found

    mid = (left + right) // 2

    # Check if target is at mid
    if arr[mid] == target:
        return mid

    # If target is greater, search right half
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)

    # If target is smaller, search left half
    else:
        return binary_search_recursive(arr, target, left, mid - 1)


# Example usage
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 7
result = binary_search_recursive(arr, target, 0, len(arr) - 1)

if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found in array")
