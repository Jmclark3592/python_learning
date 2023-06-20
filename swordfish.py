#password swordfish

while True:
    name = input("what's your name? ")
    if name.lower() != 'justin':
        continue
    password = input('what is the password? ')
    if password.lower() != "swordfish":
        continue
    else:
        break
print("access granted")