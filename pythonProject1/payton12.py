# with open("payton12.txt", "r") as file:
#     for line in file:
#         print(line.rstrip())

name = []
with open("payton12.txt") as file:
    for line in file:
            name.append(line.rstrip())

for name in sorted(name):
    print(f'{name}')
