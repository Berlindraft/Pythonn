#print squares
def print_square():
    size = int(input("Enter a size: "))
    set_size(size)

def set_size(size):
    for i in range(size):
        print(" * " * size )


print_square()