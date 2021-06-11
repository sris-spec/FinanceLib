import matplotlib.pyplot as plt


def SIgraph(P,R,T):
    TI=P*R*T/100
    I=P*R/100
    Years=[]
    SI=[]
    A=P+TI
    for i in range(T):
        Years.append(i+1)
        SI.append(I)

    # plotting the graph

    plt.plot(Years,SI)
    plt.title('Simple Interest Graph (SI V/S Years)')
    plt.xlabel('Years')
    plt.ylabel('Simple Interest')
    print("Amount deposited is:",P)
    print("Intrest earned at the end of each year is:",I)
    print("The total simple interest at the end of {} years is: {}".format(T,TI))
    print("Total Amount after {} years (at maturity) is:{}".format(T,A))
    plt.show()


def moneygraph(P,R,T):
    I=P*R/100
    TI=P*R*T/100
    A=P+TI
    Years=[]
    Money=[]
    for i in range(T):
        P=P+I
        Years.append(i+1)
        Money.append(P)

    # Plotting the graph
    plt.plot(Years,Money)
    plt.title('Money Graph')
    plt.xlabel('Years')
    plt.ylabel('Money')
    print("Amount deposited is:",P)
    print("Intrest earned at the end of each year is:",I)
    print("Tota amount at the end of {} years is: {}".format(T,A))
    print("Amount recived at maturity :",A)
    plt.show()


def ratio(P,R,T):
    TI=P*R*T/100
    deposit=P
    A=P+TI
    x=[]
    x.append(deposit)
    x.append(TI)
    x.append(A)
    names=["Deposit","Intrest","Total_Amount"]
    depexplode=[0.2,0.1,0.1]
    plt.pie(x,labels=names,explode=depexplode,autopct='%1.1f%%', shadow=True)
    plt.legend(title="Ratios:")
    plt.show() 


#P=float(input("Principal amount is:"))
#R=float(input("Rate of interest per annum is:"))
#T=int(input("time:"))
#x=SIgraph(20000,5,10)
#y=moneygraph(20000,5,10)
#z=ratio(20000,5,10)