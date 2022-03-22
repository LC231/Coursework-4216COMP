import csv
from datetime import date, datetime
from itertools import count
import matplotlib.pyplot as plt



filename = 'Coursework-4216COMP-1/data.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
    def LAT():
        dates,LAT_Uncertainty = [],[]
        
        for row in reader:
    
            temp_date = datetime.strptime(row[1],'%d/%m/%Y')
            dates.append(temp_date)

            temp_LAT_Uncertainty = float(row[3])
            LAT_Uncertainty.append(temp_LAT_Uncertainty)

        dates = dates[::2]
        LAT_Uncertainty = LAT_Uncertainty[::2]

        plt.style.use('seaborn')
        fig, ax = plt.subplots()
        ax.plot(dates,LAT_Uncertainty,c='green')


        ax.set_title("Graph")
        ax.set_xlabel('Temperature (F)')
        fig.autofmt_xdate()
        ax.set_ylabel("Land Average Temperature Uncertainty")
        
        
        ax.set_ylim(0,0.45)
        #ax.set_xticks(range(1900,2015,10))
        plt.show()

        

    LAT()
