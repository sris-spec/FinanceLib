
def emi_calculator(P,R,T):
    R = R / (12 * 100) # one month interest
    emi = P* R * ((1+R)**T)/((1+R)**T - 1)
    Loantaken=P
    print("Monthly Repayment (EMI) is : ",emi)
    print("Loan Taken: ",P)
    
 




# P = float(input("Enter principal (loan) amount:"))
# R = float(input("Enter annual interest rate:"))
# T = int(input("Enter number of months:" ))

# x=emi_calculator(P,R,T)


