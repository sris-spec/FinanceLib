from typing import List
import matplotlib.pyplot as plt

def FD(Principle :int,Rate :float,Time :int,freq :str) ->None:
    
    
    """
    Calculates and Visualises Fixed Deposit(FD)
    
    Parameters:
     Principle(int) : FD Amount
     Rate(float) : Rate of Interest(in percentage)
     Time(int) : Number of years for which Fd is created
     freq(str) : The frequency in which compound interest should be calculated.
                 The values can be from the list: ("annually","quaterly","monthly")
     
    Returns:
     Return type: void
      
    Example:
     FD(50000,10.5,5,Yearly)
     
     """
     
    #Required list for plotting Graph and pie chart
    fd_amount : int=Principle
    closing_balance : List[float]=[]
    interest_data : List[float]=[]
    year :List[float]=[]
    
    fig, (ax1,ax2,ax3)=plt.subplots(3)
    fig.suptitle('Fixed Deposit')
       
    if(freq== "annually"):

        for i in range(Time):
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
        ax1.pie(x,autopct ='%.1f',labels = mylabels,explode = myexplode,shadow=True)
        ax1.legend()
        ax1.set_title("Yearly Cummulated")
        


        # Bar graph for Balance
        ax2.bar(year,closing_balance,color="#800000")
        ax2.set_title("FD Amount over the Year(Annually)")
        ax2.set_xlabel("Years")
        ax2.set_ylabel("Balance")
        
        

        # Bar graph for interest 
        ax3.bar(year,interest_data)
        ax3.set_title("Interest earned over the Year(Annually)")
        ax3.set_xlabel("Years")
        ax3.set_xlabel("Interest")

        plt.tight_layout()
        plt.show()




    elif (freq == "quaterly"):

        for i in range(Time):
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
        ax1.pie(x,autopct ='%.1f',labels = mylabels,explode = myexplode,shadow=True)
        ax1.legend()
        ax1.set_title("Quaterly Cummulated")
        

        
        # Bar graph for Balance
        ax2.bar(year,closing_balance,color="#800000")
        ax2.set_title("FD Amount over the Year(Quaterly)")
        ax2.set_xlabel("Years")
        ax2.set_ylabel("Balance")
        


        # Bar graph for interest 
        plt.bar(year,interest_data)
        ax3.set_title("Interest earned over the Year(Quaterly)")
        ax3.set_xlabel("Years")
        ax3.set_ylabel("Interest")
        plt.tight_layout()
        plt.show()
        



    elif (freq == "monthly"):
        for i in range(Time):
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
        ax1.pie(x,autopct ='%.1f',labels = mylabels,explode = myexplode,shadow=True)
        ax1.legend()
        ax1.set_title("Monthly Cummulated")
        

        # Bar graph for Balance
        ax2.bar(year,closing_balance,color="#800000")
        ax2.set_title("FD Amount over the Period(Monthly)")
        ax2.set_xlabel("Years")
        ax2.set_ylabel("Balance")
        


        # Bar graph for interest 
        ax3.bar(year,interest_data)
        ax3.set_title("Interest earned over the Year(monthly)")
        ax3.set_xlabel("Years")
        ax3.set_ylabel("Interest")
        plt.tight_layout()
        plt.show()
#FD(50000,10.5,5,'Yearly')        







   
