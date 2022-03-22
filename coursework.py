import csv
from datetime import date, datetime
import matplotlib.pyplot as plt


filename = 'Coursework-4216COMP-1/data.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
    def LAT():
        date,LAT_Uncertainty = [],[]
        for row in reader:
    
            temp_date = datetime.strptime(row[1],'%d/%m/%Y')
            date.append(temp_date)

            temp_LAT_Uncertainty = float(row[3])
            LAT_Uncertainty.append(temp_LAT_Uncertainty)
            #print(row[1]+"\t"+row[3])

    
        plt.style.use('seaborn')
        fig, ax = plt.subplots()
        ax.plot(date,LAT_Uncertainty, c='red')


        ax.set_title("Graph", fontsize=24)
        ax.set_xlabel('Land Average Temperature Uncertainty', fontsize=10)
        fig.autofmt_xdate()
        ax.set_ylabel("Temperature (F)", fontsize=10)
        ax.tick_params(axis='both', which='major', labelsize=16)
        

        plt.show()
    LAT()
