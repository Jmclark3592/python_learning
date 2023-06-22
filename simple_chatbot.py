#simple chatbot

name = input("hello what's your name? ")
print(f"hello, {name}, how are you?")
feel = input()

if 'good' in feel:
    print("that's great!")
elif 'okay' or 'alright' in feel:
    print("right on")
else:
    print("Hey you can always make it better")

print('What are you doing today?')
what = input()
if 'friends' in what:
    print("we love friends")
else:
    print('sounds like a lovely day')

print('well i have tons of robot stuff to do, take care!')