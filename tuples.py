

spam = ['A', 'B', 'C', 'D']

def commas(letters):
    return ', '.join(letters[:-1]) + ", and " + letters[-1]

print(commas(spam))