import csv

filename = 'data.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    print(header_row)
    
    for index, column_header in enumerate(header_row):
        print(index, column_header)#

