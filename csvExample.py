import csv
print('----learning how to read csv----')
file = open('example.csv')
reader = csv.reader(file)
for row in reader:
    print(str(reader.line_num) + str(row))
print(" ")
print('----learning how to write a new csv----')
#file2 = open('output.csv', 'w')
#list2 = csv.writer(file2)
#list2.writerow(['spam', 'eggs', 'bacon', 'ham'])
#list2.writerow(['hello', 'world', 'eggs', 'bacon', 'ham'])
#list2.writerow([1, 2, 3.14, 4])
#file2.close()
print('----was successful!!----')