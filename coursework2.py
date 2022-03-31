import csv
import matplotlib.pyplot as plt
from datetime import datetime
import numpy as np

with open('data.csv') as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
    def max_Temp():
        max_temps, min_temps, dates = [],[],[]
        
        for row in reader:
            max_temp = float(row[8])
            min_temp = float(row[9])

            min_temps.append(min_temp)
            max_temps.append(max_temp)
            date = datetime.strptime(row[1],'%d/%m/%Y')
            dates.append(date)
            
        dates=dates[::10]
        max_temps = max_temps[::10]
        min_temps = min_temps[::10]

#Create extra plots

#New test
        fig, ax = plt.subplots()
        ax.plot(dates, max_temps, c='red')

        ax.set_title("Land and Ocean average temperature", fontsize=15)
        ax.set_xlabel('Dates', fontsize=16)
        fig.autofmt_xdate()
        ax.set_ylabel("Temperature (F)", fontsize=16)

        plt.show()
    
    max_Temp()   
