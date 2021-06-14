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
#EMI(500000,10.5,2)    