import csv

inputCredit = open('/Users/alishan/tmp/credit_data.csv')
inputDebit = open('/Users/alishan/tmp/debit_data.csv')
outputFile  = open('/Users/alishan/Nextcloud/Projects/Hisaab/combined_data.csv', 'w', newline='')

creditReader = csv.reader(inputCredit)
debitReader = csv.reader(inputDebit)
combinedWriter = csv.writer(outputFile)

print('Combining Credit and Debit CSV File ...')
for row in debitReader:
    if row[1] == 'Amount':
        combinedWriter.writerow(row)
    else:
        combinedWriter.writerow(row)

for row in creditReader:
    if row[1] != 'Amount':
        combinedWriter.writerow(row)
        
inputCredit.close()
inputDebit.close()
outputFile.close()
