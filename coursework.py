
import csv
import matplotlib.pyplot as plt
from datetime import datetime

with open('M:\Coursework-4216COMP\data.csv') as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
    for index, column_header in enumerate(header_row):
        print(index, column_header)
    
    #----------------------------LUKE 1
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
        ax.plot(dates, max_temps,'ok-')

  
        ax.set_title("Max Temperatures", fontsize=24)
        ax.set_xlabel('Dates(years)', fontsize=16)
        fig.autofmt_xdate()
        ax.set_ylabel("Temperature (C)", fontsize=16)
        ax.tick_params(axis='both', which='major', labelsize=16)
        ax.set_yticks(range(1,26,2))
        ax.set_ylim(1,26)
        
        plt.show()  
      
    
    #----------------------------ETHAN
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
        ax.set_xlabel('Dates(years)', fontsize=16)
        fig.autofmt_xdate()
        ax.set_ylabel("Measurement Uncertainty (MU)", fontsize=16)
        ax.tick_params(axis='both', which='major', labelsize=16)
        ax.set_ylim(0,0.75)
        
        plt.show()  


    #----------------------------SHANE
    def LATU():

        #OPTIONS---------
        def options():

            user_clarity="" 
            graph_type=""

            while True:
                print("\nGRAPH TYPE:")
                print("1 - Line")
                print("2 - Scatter")
                
                graph_type = input("Choice: ") 
                if graph_type == '1' or graph_type == '2':

                    break
                else:
                    print("Invalid Entry.")

            
            while True:
                user_clarity = input("Improve clarity? (Y/N): ") 
                user_clarity = user_clarity.upper()   
                if user_clarity == 'Y':

                    break
                elif user_clarity == 'N':
                    
                    break
                else:
                    print("Invalid Entry.")


            graph(user_clarity,graph_type)       


        #MAIN---------
        def graph(option1,option2):
            dates,LAT_Uncertainty = [],[]
            

            f.seek(0)
            next(reader)
            
            for row in reader:
        
                temp_date = datetime.strptime(row[1],'%d/%m/%Y')
                dates.append(temp_date)

                temp_LAT_Uncertainty = float(row[3])
                LAT_Uncertainty.append(temp_LAT_Uncertainty)

            #Clarity
            if option1 == 'Y':
                dates = dates[::2]
                LAT_Uncertainty = LAT_Uncertainty[::2]
            
        
            plt.style.use('seaborn')
            fig, ax = plt.subplots()

            #Style
            if option2 == '2':
                ax.set_title("Land Average Temperature Uncertainty (Scatter Plot)")
                ax.scatter(dates,LAT_Uncertainty)
            else:
                ax.set_title("Land Average Temperature Uncertainty (Line Graph)")
                ax.plot(dates,LAT_Uncertainty,c='green') 
            


            
            ax.set_xlabel('Date (Year)')
            fig.autofmt_xdate()
            ax.set_ylabel("Measurement Uncertainty (MU)")
            
        
            ax.set_ylim(0,0.45)
            plt.show()
            options()
            
        #CALL---------
        options()



    
           
print("1 = Land Average Temperature")
print("2 = Land Average Tmeprature Uncertainty")
print("3 = Land Max Temperature")
print("4 = Land Max Temperature Uncertainty")
print("5 = Land Min Temperature")
print("6 = Land Min Temperature uncertainty")
print("7 = Land and Ocean Average Temperature")
print("8 = Land and Ocean Average Temperature Uncertainty")
# choice = input("Please enter a number between 1-8:")

# if choice == '1':
#     elif choice =='2':
#         elif choice =='3':
#             elif choice =='4':
#                 elif choice =='5':
#                     elif choice =='6':
#                         elif choice =='7':
#                             elif choice =='8':

