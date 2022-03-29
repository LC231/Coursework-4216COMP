import csv
from datetime import date, datetime
from email import message
from itertools import count
from click import option
import matplotlib.pyplot as plt



filename = 'Coursework-4216COMP-1/data.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
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

    LATU()

   
    
   
