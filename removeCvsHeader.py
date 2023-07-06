#! python3

import csv, os
os.makedirs('headerRemoved', exist_ok=True)

for filename in os.listdir('.'):
    if not filename.endswith('.csv'):
        continue

    print('removing header from ' + filename + '...')

    rows = [] #creates new list
    fileObj = open(filename)
    readerObj = csv.reader(fileObj)
    for row in readerObj:
        if readerObj.line_num ==1:
            continue
        rows.append(row) #appends old list into new list (minus first row)
    fileObj.close()

    fileObj = open(os.path.join('headerRemoved', filename), 'w')
    writer = csv.writer(fileObj)
    for row in rows:
        writer.writerow(row)
    fileObj.close()