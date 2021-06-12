import matplotlib.pyplot as plt

def FD(Principle :int,Rate :float,Time :int,freq :str) ->None:
    
    
    """
    Calculates and Visualises Fixed Deposit(FD)
    
    Parameters:
     Principle(int) : FD Amount
     Rate(float) : Rate of Interest(in percentage)
     Time(int) : Number of years for which Fd is created
     freq(str) : The frequency in which compound interest should be calculated.
                 The values can be from the list: ("Yearly","Quaterly","Monthly")
     
    Return:
     The function has void return type.
      
    Example:
     FD(50000,10.5,5,Yearly)
     
     """
     
    #Required list for plotting Graph and pie chart
    fd_amount=Principle
    closing_balance=[]
    interest_data=[]
    year=[]
    
   
    if(freq== "Yearly"):

        for i in range(T):
            a=Principle*(1+Rate/100)**1
            year.append(i+1)
            closing_balance.append(a)
            interest_data.append(a-Principle)
            Principle=a
            print("Interest Earned at the end of : ")
            print("Year {} is : {} ".format(i+1,round(interest_data[i])))
            
        #printing final data
        print("\n\n")
        print("Amount Deposited : ",fd_amount)
        print("Maturity Amount : ",round(closing_balance[-1]))
        print("Interest Earned : ",round(sum(interest_data)))
       
       
        # Pie chart
        x=[fd_amount,sum(interest_data)]
        mylabels=("FD amount","Interest Earned")
        myexplode=[0,0.2]
        plt.pie(x,autopct ='%.1f',labels = mylabels,explode = myexplode,shadow=True)
        plt.legend()
        plt.title("Yearly Cummulated")
        plt.show()


        # Bar graph for Balance
        plt.bar(year,closing_balance,color="#800000")
        plt.title("FD Amount over the Year(Yearly)")
        plt.xlabel("Years")
        plt.ylabel("Balance")
        plt.show()

        # Bar graph for interest 
        plt.bar(year,interest_data)
        plt.title("Interest earned over the Year(Yearly)")
        plt.xlabel("Years")
        plt.ylabel("Interest")
        plt.show()




    elif (freq == "Quaterly"):

        for i in range(T):
            a=Principle*(1+Rate/400)**4
            year.append(i+1)
            closing_balance.append(a)
            interest_data.append(a-Principle)
            Principle=a
            print("Interest Earned at the end of : ")
            print("Year {} is : {} ".format(i+1,round(interest_data[i])))
            
        #printing final data
        print("\n\n")
        print("Amount Deposited : ",fd_amount)
        print("Maturity Amount : ",round(closing_balance[-1]))
        print("Interest Earned : ",round(sum(interest_data)))
     
        

        #Pie chart
        x=[fd_amount,sum(interest_data)]
        mylabels=("FD amount","Interest Earned")
        myexplode=[0,0.2]
        plt.pie(x,autopct ='%.1f',labels = mylabels,explode = myexplode,shadow=True)
        plt.legend()
        plt.title("Quaterly Cummulated")
        plt.show()

        
        # Bar graph for Balance
        plt.bar(year,closing_balance,color="#800000")
        plt.title("FD Amount over the Year(Quaterly)")
        plt.xlabel("Years")
        plt.ylabel("Balance")
        plt.show()


        # Bar graph for interest 
        plt.bar(year,interest_data)
        plt.title("Interest earned over the Year(Quaterly)")
        plt.xlabel("Years")
        plt.ylabel("Interest")
        plt.show()



    elif (freq == "Monthly"):
        for i in range(T):
            a=Principle*(1+Rate/1200)**12
            year.append(i+1)
            closing_balance.append(a)
            interest_data.append(a-Principle)
            Principle=a

            print("Interest Earned at the end of : ")
            print("Year {} is : {}".format(i+1,round(interest_data[i])))
            
        #Printing final data
        print("\n\n")
        print("Amount Deposited : ",fd_amount)
        print("Maturity Amount : ",round(closing_balance[-1]))
        print("Interest Earned : ",round(sum(interest_data)))
        
       
        # Pie chart 
        x=[fd_amount,sum(interest_data)]
        mylabels=("FD amount","Interest Earned")
        myexplode=[0,0.2]
        plt.pie(x,autopct ='%.1f',labels = mylabels,explode = myexplode,shadow=True)
        plt.legend()
        plt.title("Monthly Cummulated")
        plt.show()

        # Bar graph for Balance
        plt.bar(year,closing_balance,color="#800000")
        plt.title("FD Amount over the Period(Monthly)")
        plt.xlabel("Years")
        plt.ylabel("Balance")
        plt.show()


        # Bar graph for interest 
        plt.bar(year,interest_data)
        plt.title("Interest earned over the Year(monthly)")
        plt.xlabel("Years")
        plt.ylabel("Interest")
        plt.show()






   
