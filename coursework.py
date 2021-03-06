
import csv
import matplotlib.pyplot as plt
from datetime import datetime

with open('Coursework-4216COMP/data.csv') as f:
    reader = csv.reader(f)
    header_row = next(reader)


    
    #----------------------------LUKE 1
    def LMT():
        max_temps, dates = [],[]
        
        f.seek(0)
        next(reader)

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
        mainmenu()
      
    
    #----------------------------ETHAN
    def LMTU():
        lmtus, dates = [],[]
        
        f.seek(0)
        next(reader)

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
        mainmenu() 


    
    #----------------------------NIAMH
    def LAT():
        landAves, dates = [],[]
        
        f.seek(0)
        next(reader)
        
        for row in reader:
            landAve = float(row[2])
            landAves.append(landAve)
            date = datetime.strptime(row[1],'%d/%m/%Y')
            dates.append(date)
            
        dates=dates[::10]
        landAves = landAves[::10]
        
        plt.style.use('seaborn-dark-palette')
        fig, ax = plt.subplots()
        ax.plot(dates, landAves, c='red')

        ax.set_title("Monthly Average Land Temperatures", fontsize=20)
        ax.set_xlabel('Date', fontsize=14)
        fig.autofmt_xdate()
        ax.set_ylabel("Temperature (C)", fontsize=14)
        ax.tick_params(axis='both', which='major', labelsize=14)
        ax.set_yticks(range(1,26,2))
        ax.set_ylim(1,26)
        
        plt.show()   
        mainmenu()
    
    

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
            mainmenu()
            
            
        #CALL---------
        options()


   #----------------------------LUKE 2

    def LOAT():

        max_temps, dates = [],[]
        f.seek(0)
        next(reader)
        for row in reader:

            max_temp = float(row[8])                
            max_temps.append(max_temp)

            date = datetime.strptime(row[1],'%d/%m/%Y')
            dates.append(date)
            
        dates=dates[::10]
        max_temps = max_temps[::10]


            #Create extra plots

            #New test
        fig, ax = plt.subplots()
        ax.plot(dates, max_temps, c='red')

        ax.set_title("Land and Ocean average temperature", fontsize=15)
        ax.set_xlabel('Dates', fontsize=16)
        fig.autofmt_xdate()
        ax.set_ylabel("Temperature (F)", fontsize=16)

        plt.show()
    
         
        mainmenu()

    def LOATU():
        min_temps, dates = [],[]
        f.seek(0)
        next(reader)
        for row in reader:
                
            min_temp = float(row[9])
            min_temps.append(min_temp)
                
            date = datetime.strptime(row[1],'%d/%m/%Y')
            dates.append(date)
                
        dates=dates[::10]
            
        min_temps = min_temps[::10]

            #Create extra plots

            #New test
        fig, ax = plt.subplots()
        ax.plot(dates, min_temps, c='blue')

        ax.set_title("Land and Ocean average temperature uncertainty", fontsize=15)
        ax.set_xlabel('Dates', fontsize=16)
        fig.autofmt_xdate()
        ax.set_ylabel("Temperature (F)", fontsize=16)

        plt.show()
        
          
        mainmenu()








    #----------------------------LAURA
    def LMNT():
            min_temps, dates = [],[]
            
            f.seek(0)
            next(reader)

            for row in reader:
                min_temp = float(row[6])
                min_temps.append(min_temp)
                date = datetime.strptime(row[1],'%d/%m/%Y')
                dates.append(date)
                

            dates=dates[::10]
            min_temps = min_temps[::10]
            
            plt.style.use('seaborn')
            fig, ax = plt.subplots()
            ax.plot(dates, min_temps,'*b-')

    
            ax.set_title("Min Temperatures", fontsize=24)
            ax.set_xlabel('Dates(years)', fontsize=16)
            fig.autofmt_xdate()
            ax.set_ylabel("Temperature (C)", fontsize=16)
            ax.tick_params(axis='both', which='major', labelsize=16)
            ax.set_yticks(range(-5,12,2))
            ax.set_ylim(-5,12)
            
            plt.show()  
            mainmenu()














    def mainmenu():    

        print("1 = Land Max Temperature")
        print("2 = Land Max Temperature Uncertainty")
        print("3 = Land Average Temperature")
        print("4 = Land Average Tmeprature Uncertainty")
        print("5 = Land Min Temperature")
        print("6 = Land Min Temperature uncertainty")
        print("7 = Land and Ocean Average Temperature")
        print("8 = Land and Ocean Average Temperature Uncertainty")
        choice = input("Please enter a number between 1-8:")

        if choice == '1':
            LMT()
        elif choice =='2':
            LMTU()
        elif choice =='3':
            LAT()
        elif choice =='4':
            LATU()
        elif choice =='5':
            LMNT()
            ##
        elif choice =='7':
            LOAT()
        elif choice =='8':
            LOATU()


    mainmenu()




