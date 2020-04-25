import csv
import re
import Filters
import glob
import os


all_credit_files = glob.glob('/Users/alishan/Downloads/AXXXX_XXXX_XXXX_1720*.csv')
latest_file = max(all_credit_files, key=os.path.getctime)
inputFile = open(latest_file)
outputFile  = open('/Users/alishan/tmp/credit_data.csv', 'w', newline='')

reader = csv.reader(inputFile)
writer = csv.writer(outputFile)

print('Creating Credit CSV ...')
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
            if re.match("^{0}".format(n.upper()), temp[2]):
                temp.append(c)
        writer.writerow(temp)
        
inputFile.close()
outputFile.close()
