import matplotlib.pyplot as plt
from typing import List

def EMI(principal :int,rate :float,tenure :int) ->None:
    
    """
    Calculates and visualises Equated Monthly Interest(EMI)

    Parameters:
      principal(float) : principal amount 
      rate(float) : Rate of interest
      tenure(int) : number of years for which EMI has to be calculated

    Return:
      The function has void return type.

    Example:
       EMI(500000,10.5,2)

    """

    rate : float= rate/(12*100) #rate of interest 
    tenure : float= tenure * 12 # no of months
    emi :float = round((principal * rate * pow(1+rate,tenure))/(pow(1+rate,tenure)-1),0)
    print("Loan EMI: ",emi)
    
    # total amount to be paid after the mentioned tenure
    total_amt : float = emi * tenure 
    interest : float= round((total_amt - principal)*100/total_amt,0)
    loan_amt: float= principal * 100/total_amt
    print("Total Payment: ",total_amt)
    print("Total Interest Payable: ",total_amt - principal)
    
    # plotting interest and principal in a pie chart
    fig1, (ax1,ax2)= plt.subplots(2)
    fig1.suptitle('EMI')
    fig2,(ax3)=plt.subplots()
    fig2.suptitle('Month-wise Details')
    x = [loan_amt,interest]
    mylabels = ("Principal Loan Amount","Interest")
    myexplode = [0,0.2]
    ax1.pie(x,autopct ='%.1f',labels = mylabels,explode = myexplode)
    ax2.legend()
    
    
    # required lists for plotting graph and table
    interest_data :List[float]=[]
    principal_data: List[float]=[]
    balance_data: List[float]=[]
    month_no : List[float]= []
    cell_text :List[float]=[]
    columns = ["Month_No","Principal","Interest","Balance"]
    prev_bal = principal
    
    # finding monthly principal and interest
    for i in range(tenure):
        month_interest = round(prev_bal*rate,0)
        month_principal = emi - month_interest
        prev_bal = prev_bal - month_principal
        
        interest_data.append(month_interest)
        principal_data.append(month_principal)
        balance_data.append(prev_bal)
        month_no.append(i+1)
        cell_text.append([i+1,month_principal,month_interest,prev_bal])
        
    # plotting bar graph
    
    ax2.bar(month_no, principal_data, width=0.35, label='Principal')
    ax2.bar(month_no, interest_data, width=0.35, bottom=principal_data,
       label='Interest')
    ax2.set_xlabel('Months')
    ax2.set_ylabel('EMI Payment')
    ax2.set_title('EMI Payment/month')
    ax2.legend()
    
    
    
    # Table creation
    
    ax3.set_axis_off()
    table = ax3.table(cellText= cell_text,colLabels=columns,loc='upper center',cellLoc='center')
    
    table.set_fontsize(10)
    table.scale(2,2)
    plt.tight_layout()
    plt.show()


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
        ax1.set_title("Annually Cummulated")
        


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