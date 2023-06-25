#practice

def get_formatted_name(first_name, last_name):
    full_name = f"{first_name} {last_name}"
    return full_name.title()

while True:
    print("Please tell me your name (enter q to quit)")
    f_name = input("First name: ")
    l_name = input('Last name: ')
    if f_name == 'q':
        break
    if l_name == 'q':
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print(f"Hello, {formatted_name}")
