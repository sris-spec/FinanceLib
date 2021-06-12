import matplotlib.pyplot as plt

def Compound_Interest(P :int,R :float,T :int,freq :str) -> None:
    
    
    """
     Calculates and visualises compound interest 

     Parameters:
        P(float) : Principal amount
        R(float) : Rate of interest
        T(int) : Time
        freq(str) : The frequency in which compound interest should be calculated. 
                    The values can be from the list: ('annually','semiannually','quaterly','monthly')

    Return:
        This function does not return anything.
    
    Example:
       Compound_Interest(20000,4.5,5,'quaterly')
        
    """


    # defining required lists
    interest = []
    time = []
    Amount = []
    deposit=P
    TI=0
    
    # compound interest calculation along with graphical representation 
    if(freq=='monthly'):
        for i in range(12*T):
            I = P * R/1200
            P = P + I
            TI+=I
            print("Interest recieved in month {} is {}".format(i+1,I))
            interest.append(I)
            time.append(i+1)
            Amount.append(P)
        print("In {} years you will have {} if interest is compounded {} ".format(T,P,freq))
        plt.plot(time,Amount)
        plt.xlabel("Months")
        plt.ylabel("Amount")
        plt.show()
        
        x=[]
        x.append(deposit)
        x.append(TI)
        names=["Deposit","Interest"]
        depexplode=[0,0.2]
        plt.pie(x,labels=names,explode=depexplode , shadow=True)
        plt.legend(title="Ratios:")
        plt.show()  
        
    elif (freq == 'annually'):
        for i in range(T):
            I = P * R/100
            P = P + I
            TI+=I
            print("Interest recieved in year {} is {}".format(i+1,I))
            interest.append(I)
            time.append(i+1)
            Amount.append(P)
        print("In {} years you will have {} if interest is compounded {} ".format(T,P,freq))
        plt.plot(time,Amount)
        plt.xlabel("Years")
        plt.ylabel("Amount")
        plt.show()
         
        x=[]
        x.append(deposit)
        x.append(TI)
        names=["Deposit","Interest"]
        depexplode=[0,0.2]
        plt.pie(x,labels=names,explode=depexplode , shadow=True)
        plt.legend(title="Ratios:")
        plt.show() 
        
    elif (freq == 'quaterly'):
        for i in range(4*T):
            I = P * R/400
            P = P + I
            TI+=I
            print("Interest recieved in quarter year {} is {}".format(i+1,I))
            interest.append(I)
            time.append(i+1)
            Amount.append(P)
        print("In {} years you will have {} if interest is compounded {} ".format(T,P,freq))
        plt.plot(time,Amount)
        plt.xlabel("Quarter Years")
        plt.ylabel("Amount")
        plt.show()
        
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
            I = P * R/200
            P = P + I
            TI+=I
            print("Interest recieved in semi year {} is {}".format(i+1,I))
            interest.append(I)
            time.append(i+1)
            Amount.append(P)
        print("In {} years you will have {} if interest is compounded {} ".format(T,P,freq))
        plt.plot(time,Amount)
        plt.xlabel("Semi Years")
        plt.ylabel("Amount")
        plt.show()
        
        x=[]
        x.append(deposit)
        x.append(TI)
        names=["Deposit","Interest"]
        depexplode=[0,0.2]
        plt.pie(x,labels=names,explode=depexplode , shadow=True)
        plt.legend(title="Ratios:")
        plt.show() 