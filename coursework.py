
import csv
import matplotlib.pyplot as plt


with open('M:/4216COMP coursework/Coursework-4216COMP/data.csv') as f:
    reader = csv.reader(f)
    header_row = next(reader)
    print(header_row)
    
    for index, column_header in enumerate(header_row):
        print(index, column_header)#
