
def collatz(number):
    if number % 2 == 0:
        print(number // 2)
        return
    else:
        print(3 * number + 1)
        return

inputValue = input("input a number: ")

r = input(inputValue)

while True:
    collatz(r)