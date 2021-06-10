import matplotlib.pyplot as plt
import math

def EMI(principal,rate,tenure):
    rate = rate/(12*100) #rate of interest 
    tenure = tenure * 12 # no of months
    emi = round((principal * rate * pow(1+rate,tenure))/(pow(1+rate,tenure)-1),0)
    print("Loan EMI: ",emi)
    
    # total amount to be paid after the mentioned tenure
    total_amt = emi * tenure 
    interest = round((total_amt - principal)*100/total_amt,0)
    loan_amt = principal * 100/total_amt
    print("Total Payment: ",total_amt)
    print("Total Interest Payable: ",total_amt - principal)
    
    # plotting interest and principal in a pie chart
    x = [loan_amt,interest]
    mylabels = ("Principal Loan Amount","Interest")
    myexplode = [0,0.2]
    plt.pie(x,autopct ='%.1f',labels = mylabels,explode = myexplode)
    plt.legend()
    plt.show()
    
    # required lists for plotting graph and table
    interest_data=[]
    principal_data=[]
    balance_data=[]
    month_no = []
    cell_text=[]
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
    fig, ax = plt.subplots()
    ax.bar(month_no, principal_data, width=0.35, label='Principal')
    ax.bar(month_no, interest_data, width=0.35, bottom=principal_data,
       label='Interest')
    ax.set_xlabel('Months')
    ax.set_ylabel('EMI Payment')
    ax.set_title('EMI Payment/month')
    ax.legend()
    plt.show()
    
    # Table creation
    fig, ax=plt.subplots()
    ax.set_axis_off()
    table = ax.table(cellText= cell_text,colLabels=columns,loc='upper center',cellLoc='center')
    ax.set_title('Month-wise Details')
    table.set_fontsize(10)
    table.scale(2,2)
    plt.show()
    

    
# Example - EMI(500000,10.5,2)