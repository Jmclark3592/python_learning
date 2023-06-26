#fantasy game - print the invesntory and also number of items

stuff = {'rope' : 1, 'torch' : 6, 'gold coin' : 42, 'dagger' : 1, 'arrow' : 12,}

print("Inventory: ")
def displayInventory(inventory):
    count = 0
    for k, v in inventory.items():
        count = count + v
        print(f"{k.title()} : {v}")
    print(f"Total number of items {count}")

print(displayInventory(stuff))

#dragon loot - create a function that turns this list into a dictionary where key is loot and value is number of each

print('''more loot''')

dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

print(dragonLoot[0:3])