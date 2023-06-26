#adventure game

def encountered_dead_end(dead_end): #function to fill in with road blocks like encountered_dead_end('a mysterious man')
    print(f"You have encountered {dead_end} and must turn back.")

def encountered_item(item): #function to fill in with item you find like encountered_item('a hat')
    print(f"You see {item} on the ground. You pick it up.")

def look_around(item, path):
        

print("adventurer finds himself in a room\n")


while True:
    choice = input("What do you want to do?\n"
               "OPTIONS: Look around, Go East/West/North/South, Pick up (item)")

    if choice.lower() == 'pick up item':
        print("You find nothing of value.")
    if choice.lower() == 'go east':
        print("you go East")
    if choice.lower() == 'go west':
        print("you go West")
    if choice.lower() == 'go north':
        print("you go North")
    if choice.lower() == 'go south':
        print("you go South")
    if choice.lower() == 'look aroud':
        print("you see nothing of value")
    else:
        print("invalid choice")
