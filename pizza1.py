#coding

def make_pizza(size, *toppings):
    print(f"making {size} pizza with the following toppings: ")
    for topping in toppings:
        print(topping)

