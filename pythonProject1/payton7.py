# boolean while loops

def get_integer():
    while True:
        try:
            return int(input("what is x: "))
        except ValueError:
            print('Error')


x = get_integer()
print(f'x is {x}\n' * x)
