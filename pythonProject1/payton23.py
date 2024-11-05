# RECURSIONS
# ZYRON

def draw_line(tick_length, tick_label=''):
    """
    Draw a single line with given tick length (and an optional label).
    """
    line = '-' * tick_length
    if tick_label:
        line += ' ' + tick_label
    print(line)

def draw_interval(center_length):
    """
    Draw the ticks for a ruler's interval recursively.
    """
    if center_length > 0:  # Base case: Do nothing for length 0
        draw_interval(center_length - 1)  # Recursively draw top interval
        draw_line(center_length)  # Draw center tick
        draw_interval(center_length - 1)  # Recursively draw bottom interval

def draw_ruler(num_inches, major_tick_length):
    """
    Draw an English ruler with given number of inches and major tick length.
    """
    draw_line(major_tick_length, '0')  # Draw inch 0 line
    for i in range(1, num_inches + 1):
        draw_interval(major_tick_length - 1)  # Draw the interval of ticks
        draw_line(major_tick_length, str(i))  # Draw inch line and label

# Example usage
draw_ruler(3, 4)


def binary_search(arr, target, low, high):
    """
    Perform binary search recursively to find the target in the sorted array.
    """
    if low > high:  # Base case: Target is not found
        return -1

    mid = (low + high) // 2

    if arr[mid] == target:  # Target is found
        return mid
    elif arr[mid] > target:  # Search in the left half
        return binary_search(arr, target, low, mid - 1)
    else:  # Search in the right half
        return binary_search(arr, target, mid + 1, high)


# Example usage
arr = [1, 3, 5, 7, 9, 11, 13, 15]
target = 7
result = binary_search(arr, target, 0, len(arr) - 1)
if result != -1:
    print(f"Target {target} found at index {result}")
else:
    print(f"Target {target} not found")



def factorial(n):
    """
    Calculate the factorial of n using recursion.
    """
    if n == 0:  # Base case: factorial(0) = 1
        return 1
    else:
        return n * factorial(n - 1)  # Recursive case

# Example usage
n = 5
result = factorial(n)
print(f"Factorial of {n} is: {result}")
