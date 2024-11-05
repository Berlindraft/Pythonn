my_dict = {'a': 10, 'b': 15, 'c': 5}

# Increasing each value by 5
updated_dict = list(map(lambda item: item + 5, my_dict.values()))

print(updated_dict)
