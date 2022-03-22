
import csv
import matplotlib.pyplot as plt
from datetime import datetime

with open('M:/4216COMP coursework/Coursework-4216COMP/data.csv') as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
    def max_Temp():
        max_temps, dates = [],[]
        for row in reader:
            max_temp = float(row[4])
            max_temps.append(max_temp)
            date = datetime.strptime(row[1],'%d/%m/%Y')
            dates.append(date)

         
        plt.style.use('seaborn')
        fig, ax = plt.subplots()
        ax.plot(dates, max_temps, c='red')

  
        ax.set_title("monthly max temperatures", fontsize=24)
        ax.set_xlabel('', fontsize=16)
        fig.autofmt_xdate()
        ax.set_ylabel("Temperature (F)", fontsize=16)
        ax.tick_params(axis='both', which='major', labelsize=16)

        plt.show()  
    max_Temp()      