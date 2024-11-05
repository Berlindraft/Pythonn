# Raymund Zyron Abella, BSIT 2-B

# display items
# options to add, remove, update, display, search, exit

inventory = []
# existing inventory is given already in the program
existInventory = [
    ['shampoo', 20, 20],
    ['soap', 50, 20],
    ['toothpaste', 100, 20],
    ['toothbrush', 100, 20],
    ['conditioner', 20, 20]
]
# extended the existing inventory to the user inventory
inventory.extend(existInventory)

# shows the current inventory
print('=============INVENTORY=============')
print('Name - Price - Quantity')
for i in inventory:
    print(i[0], '\tQTY - ', i[2])

# prompts keep looping until exit is entered
while True:
    print("=============MENU=============")
    print('[ 1 ] add items to the inventory')
    print('[ 2 ] remove items to the inventory')
    print('[ 3 ] update items to the inventory')
    print('[ 4 ] display items in the inventory')
    print('[ 5 ] search items in the inventory')
    print('[ 6 ] EXIT')
    try:
        choice = int(input("Choice: ").strip())
    except:
        print('invalid input')
        break
    if choice == 1:
        # this code adds another item into the list
        name = input('Enter item name: ').strip()
        price = int(input('Enter item price: '))
        qty = int(input('Enter quantity of items: '))
        inventory.append([name, price, qty])

    elif choice == 2:
        # remove item and other data from the list
        rmv = input("Enter item to remove: ")
        for j in inventory:
            if j[0].lower() == rmv.lower():
                inventory.remove(j)
                print(f'item: "{rmv}" has been removed')

    elif choice == 3:
        # this modifies the items from the list
        name = input('Enter Item name: ').strip()
        for k in inventory:
            if k[0].lower() == name.lower():
                qty = int(input(f'Enter new quantity for {name}: ').strip())
                k[2] = qty

    elif choice == 4:
        # just prints the items in the list
        print('Inventory: ')
        print('Name - Price - Quantity')
        for i in inventory:
            print(i[0], '\tQTY - ', i[2])

    elif choice == 5:
        # searches if an item is in the inventory
        srch = input('Enter item to search: ').strip()
        for g in inventory:
            if g[0].lower() == srch.lower():
                print(f'Item: {g[0]}')
                print(f'Price: {g[1]}')
                print(f'Quantity: {g[2]}')
    elif choice == 6:
        break
    else:
        pass
