#while and for loops

#while loops to update dictionaries

food_map = {}

active = True
while active:
    name = input("\nWhat's your name? ")
    food = input("What is your favorite food? ")

    food_map[name] = food

    repeat = input('Would you like to let another person repond? (yes/no) ')
    if repeat == 'no':
        active = False

for name, food in food_map.items():
    print(f"{name} enjoys {food}")