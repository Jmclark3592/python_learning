def getSmallest(numbers):
    for num in numbers:
        smallest = sorted(numbers)
        return smallest


numb = [8, 4, 8, 99, 12]
numb1 = getSmallest(numb)
print(numb1[0])

# assert getSmallest([1, 2, 3]) == 1
# assert getSmallest([3, 2, 1]) == 1
# assert getSmallest([28, 25, 42, 2, 28]) == 2
# assert getSmallest([1]) == 1
# assert getSmallest([]) == None
