# pyramid maker
import random
from random import choice
from time import sleep


# enter height of the triangle: 6
# 1         / \
# 2        / * \
# 3       / * * \
# 4      / * * * \
# 5     / * * * * \
# 6    / _ _ _ _ _ \

def print_pyra(size):

    ast = " #"
    spc = " "
    und = " _"

    text_after = [
        "zyron",
        "raymund",
        "zy"
    ]

    another_size = size_duplicate = size

    for i in range(size):
        # rand_index = random.randint(0, len(text_after) - 1)
        # rand = text_after[rand_index]
        if size == 0:
            print(f' {spc * size_duplicate}/\\{spc * size_duplicate} | {i + 1}')
        elif i == (another_size - 1):
            print(f' /{und * i} \\{spc * size_duplicate} | {i + 1}')
        else:
            print(f'{spc * size_duplicate}/{ast * i} \\{spc * size_duplicate} | {i + 1}')
        size_duplicate -= 1


def slow_text(text, delay):
    modified_text = ''
    for char in text:
        modified_text += char
        print(char, end='', flush=True)
        sleep(delay)
    return modified_text


# Example usage
text = f'Hello {input('Enter a Name:')}\n'
delay = 0.05  # Delay in seconds
slow_text(text, delay)


def main():
    size = int(input('Enter the height of the pyramid: '))
    print_pyra(size)


if __name__ == "__main__":
    main()
