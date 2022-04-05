import csv
import matplotlib.pyplot as plt
from datetime import datetime

with open('M:/4216COMP coursework/Coursework-4216COMP/data.csv') as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
    def min_Temp():
        min_temps, dates = [],[]
        for row in reader:
            min_temp = float(row[9])
            min_temps.append(min_temp)
            date = datetime.strptime(row[1],'%d/%m/%Y')
            dates.append(date)

        dates=dates[::10]
        min_temps = min_temps[::10]
         
        plt.style.use('seaborn')
        fig, ax = plt.subplots()
        ax.plot(dates, min_temps, c='blue')

  
        ax.set_title("monthly min temperatures", fontsize=24)
        ax.set_xlabel('', fontsize=16)
        fig.autofmt_xdate()
        ax.set_ylabel("Temperature (F)", fontsize=16)
        ax.tick_params(axis='both', which='major', labelsize=16)

        plt.show()  
    min_Temp()      
