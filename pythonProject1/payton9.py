# pyramid maker

# 1          *
# 2         * *
# 3        * * *
# 4       * * * *
# 5      * * * * *
# 6     * * * * * *
# 7    * * * * * * *

def print_pyra():
    size_duplicate = size = int(input('Enter the height of the pyramid: '))
    ast = " *"
    spc = " "
    for i in range(size + 1):
        if i <= size:
            print(f'{spc * size_duplicate}{ast * i}')
            size_duplicate -= 1


print_pyra()