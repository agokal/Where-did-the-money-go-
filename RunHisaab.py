import os

import formatCSVdataDebit
import formatCSVdataCredit
import CSVdataCombine


print('Removing created files ...')
os.remove('/Users/alishan/tmp/credit_data.csv')
os.remove('/Users/alishan/tmp/debit_data.csv')
print()
print('Finished hisaab')