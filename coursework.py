
import csv
import matplotlib.pyplot as plt
from datetime import datetime

with open('M:\Coursework-4216COMP\data.csv') as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
    def max_Temp():
        max_temps, dates = [],[]
        
        for row in reader:
            max_temp = float(row[4])
            max_temps.append(max_temp)
            date = datetime.strptime(row[1],'%d/%m/%Y')
            dates.append(date)
            

        dates=dates[::10]
        max_temps = max_temps[::10]
        
        plt.style.use('seaborn')
        fig, ax = plt.subplots()
        ax.plot(dates, max_temps, c='red')

  
        ax.set_title("monthly max temperatures", fontsize=24)
        ax.set_xlabel('Dates', fontsize=16)
        fig.autofmt_xdate()
        ax.set_ylabel("Temperature (F)", fontsize=16)
        ax.tick_params(axis='both', which='major', labelsize=16)
        ax.set_yticks(range(1,26,2))
        ax.set_ylim(1,26)
        
        plt.show()  
    max_Temp()      

    def LMTU():
        lmtus, dates = [],[]
        
        for row in reader:
            lmtu = float(row[5])
            lmtus.append(lmtu)
            date = datetime.strptime(row[1],'%d/%m/%Y')
            dates.append(date)
            

        dates=dates[::10]
        lmtus = lmtus[::10]
        
        plt.style.use('seaborn')
        fig, ax = plt.subplots()
        ax.plot(dates, lmtus, 'b*-')

  
        ax.set_title("land max temperature uncertainty", fontsize=24)
        ax.set_xlabel('Dates', fontsize=16)
        fig.autofmt_xdate()
        ax.set_ylabel("Temperature (C)", fontsize=16)
        ax.tick_params(axis='both', which='major', labelsize=16)
        ax.set_ylim(0,0.75)
        
        plt.show()  
    LMTU()  