import csv
import re
import Filters
import glob
import os

#inputFile = open('/Users/alishan/Downloads/A0302960456583000-11Jan20.csv')
all_debit_files = glob.glob('/Users/alishan/Downloads/A0302960456583000*.csv')
latest_file = max(all_debit_files, key=os.path.getctime)
inputFile = open(latest_file)
outputFile  = open('/Users/alishan/tmp/debit_data.csv', 'w', newline='')

reader = csv.reader(inputFile)
writer = csv.writer(outputFile)

print('Creating Debit CSV...')
for row in reader:
    if row[1] == 'Amount':
        temp = row[:3]
        temp.append('Catagory')
        writer.writerow(temp)
    elif float(row[1])<0 and row[3] not in Filters.exclude:
        temp = row[:3]
        temp[1] = abs(float(temp[1]))
        #if temp[2] in Filters.catagories:
        for n, c in Filters.catagories.items():
            if re.match("^{0}".format(n), temp[2]):
                temp.append(c)
        writer.writerow(temp)
        
inputFile.close()
outputFile.close()
