#to do list

todo = []

while True:
    print("What do you want to do? Add, view, or delete.")
    list2 = input()
    if list2.lower() == 'add':
        item = input("what would you like to add to the list?")
        todo.append(item)
    if list2.lower() == 'view':
        print(f"you have these tasks in your Todo list: \n{todo}")
    if list2.lower() == 'delete':
        item_delete = input("what item do you want to remove?")
        todo.remove(item_delete)
    if list2.lower() != 'add' and list2.lower() != 'view' and list2.lower() != 'delete':
        print("invalid command")
