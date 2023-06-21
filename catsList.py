#lists

supplies = ['pens', 'staples', 'flamethrowers', 'binders']

name = input("what do you want to find? ")


if name.lower() not in supplies:
    print(f"you dont have {name}")
else:
    print(name + " is owned")