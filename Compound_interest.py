import matplotlib.pyplot as plt

def Compound_Interest(P,R,T,freq):
    
    #CI = p *(1+r/100)**t
    interest = []
    time = []
    Amount = []
    
    # compound interest calculation with graphical representation
    if(freq=='monthly'):
        for i in range(12*T):
            I = P * R/1200
            P = P + I
            print("Interest recieved in month {} is {}".format(i+1,I))
            interest.append(I)
            time.append(i+1)
            Amount.append(P)
        print("In {} years you will have {} if interest is compounded {} ".format(T,P,freq))
        plt.plot(time,Amount)
        plt.xlabel("Months")
        plt.ylabel("Amount")
        plt.show()
        
    elif (freq == 'annually'):
        for i in range(T):
            I = P * R/100
            P = P + I
            print("Interest recieved in year {} is {}".format(i+1,I))
            interest.append(I)
            time.append(i+1)
            Amount.append(P)
        print("In {} years you will have {} if interest is compounded {} ".format(T,P,freq))
        plt.plot(time,Amount)
        plt.xlabel("Years")
        plt.ylabel("Amount")
        plt.show()
        
    elif (freq == 'quaterly'):
        for i in range(4*T):
            I = P * R/400
            P = P + I
            print("Interest recieved in quarter year {} is {}".format(i+1,I))
            interest.append(I)
            time.append(i+1)
            Amount.append(P)
        print("In {} years you will have {} if interest is compounded {} ".format(T,P,freq))
        plt.plot(time,Amount)
        plt.xlabel("Quarter Years")
        plt.ylabel("Amount")
        plt.show()
        
    elif(freq == 'semiannually'):
        for i in range(2*T):
            I = P * R/200
            P = P + I
            print("Interest recieved in semi year {} is {}".format(i+1,I))
            interest.append(I)
            time.append(i+1)
            Amount.append(P)
        print("In {} years you will have {} if interest is compounded {} ".format(T,P,freq))
        plt.plot(time,Amount)
        plt.xlabel("Semi Years")
        plt.ylabel("Amount")
        plt.show()

# Displaying the calculated amount and interest in pie chart
def Return_Percent(P,R,T,freq):
    deposit=P
    TI=0
    
    if(freq == 'annually'):
        for i in range(T):
            I=P*R/100
            P=P+I
            TI+=I
        x=[]
        x.append(deposit)
        x.append(TI)
        names=["Deposit","Interest"]
        depexplode=[0,0.2]
        plt.pie(x,labels=names,explode=depexplode , shadow=True)
        plt.legend(title="Ratios:")
        plt.show() 
        
    elif(freq == 'monthly'):
        for i in range(12*T):
            I=P*R/1200
            P=P+I
            TI+=I
        x=[]
        x.append(deposit)
        x.append(TI)
        names=["Deposit","Interest"]
        depexplode=[0,0.2]
        plt.pie(x,labels=names,explode=depexplode , shadow=True)
        plt.legend(title="Ratios:")
        plt.show()  
        
    elif(freq == 'semiannually'):
        for i in range(2*T):
            I=P*R/200
            P=P+I
            TI+=I
        x=[]
        x.append(deposit)
        x.append(TI)
        names=["Deposit","Interest"]
        depexplode=[0,0.2]
        plt.pie(x,labels=names,explode=depexplode , shadow=True)
        plt.legend(title="Ratios:")
        plt.show()  
        
    elif(freq == 'quaterly'):
        for i in range(T):
            I=P*R/100
            P=P+I
            TI+=I
        x=[]
        x.append(deposit)
        x.append(TI)
        names=["Deposit","Interest"]
        depexplode=[0,0.2]
        plt.pie(x,labels=names,explode=depexplode , shadow=True)
        plt.legend(title="Ratios:")
        plt.show()  
        
P=float(input("Enter the deposited amount : "))
R=float(input("Enter the rate of interest per annum in percentage : "))
T=int(input("Enter the term(years) : "))
freq = input("Enter the frequency of compounding the interest:")
x=Compound_Interest(P,R,T,freq)
y=Return_Percent(P,R,T,freq)
    