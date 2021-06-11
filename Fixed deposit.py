import matplotlib.pyplot as plt

def fd(P,R,T,freq):
    
    fd_amount=P
    closing_balance=[]
    interest_data=[]
    year=[]
    
   
    if(freq == "YEARLY" or freq== "Yearly" or freq=="yearly"):

        for i in range(T):
            a=P*(1+R/100)**1
            year.append(i+1)
            closing_balance.append(a)
            interest_data.append(a-P)
            P=a
            print("Interest Earned at the end of : ")
            print("Year {} is : {} ".format(i+1,round(interest_data[i])))

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




    elif (freq == "Quaterly" or freq=="QUATERLY" or freq=="quaterly"):

        for i in range(T):
            a=P*(1+R/400)**4
            year.append(i+1)
            closing_balance.append(a)
            interest_data.append(a-P)
            P=a
            print("Interest Earned at the end of : ")
            print("Year {} is : {} ".format(i+1,round(interest_data[i])))

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



    elif (freq == "Monthly" or freq=="monthly" or freq=="MONTHLY"):
        for i in range(T):
            a=P*(1+R/1200)**12
            year.append(i+1)
            closing_balance.append(a)
            interest_data.append(a-P)
            P=a

            print("Interest Earned at the end of : ")
            print("Year {} is : {}".format(i+1,round(interest_data[i])))
            

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





# p=int(input("Enter the fd deposit amount:"))
# r=int(input("Enter the rate of interest:"))
# t=int(input("Enter the time period:"))
# freq=input("Enter the no of times deposit cummulated: ")
# x=fd(p,r,t,freq)

   