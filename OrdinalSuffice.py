number = input("Please enter a number: ")

if str(number[-2:]) in ("11", "12", "13"):
    print(f"{number}th")
elif str(number[-2:]) in ("1"):
    print(f"{number}st")
elif str(number[-2:]) in ("2"):
    print(f"{number}nd")
elif str(number[-2:]) in ("3"):
    print(f"{number}rd")
else:
    print(f"{number}th")
