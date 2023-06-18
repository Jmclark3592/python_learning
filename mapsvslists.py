#lists vs dictionaries

map1 = {'justin' : 1, 'ryan' : 2, 'roshna' : 3, }
map2 = {'justin' : 1, 'roshna' : 3, 'ryan' : 2, }

list1 = ['justin', 'ryan', 'roshna']
list2 = ['justin', 'roshna', 'ryan']

if map1 == map2:
    print("maps do not have order")
else:
    print("maps do have order")

if list1 == list2:
    print("lists do not have order")
else:
    print("lists do have order")