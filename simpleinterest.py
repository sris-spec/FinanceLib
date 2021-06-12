import matplotlib.pyplot as plt


def SI(Principle :int,Rate :float,Time: int) ->None:

    """
     Calculates and Visualises Simple Interest

     Parameters:
      Principle(int) : Principle amount
      Rate(float) : Rate of Interest(in percentage)
      Time(int) : Time period(in years)

     Return:
      This function does not return anything.

     Example:
      SI(5000,5.5,5)

    """

    #defining required lists
    Years=[]
    SI=[]
    Balance=[]


    # Simple interest calculation along with graphical representation
    Deposit=Principle
    TI=Principle*Rate*Time/100
    I=Principle*Rate/100
    A=Principle+TI


    for i in range(Time):
        Principle=Principle+I
        Balance.append(Principle)
        Years.append(i+1)
        SI.append(I)


    print("Amount deposited is:",Deposit)
    print("Intrest earned at the end of each year is:",I)
    print("Total amount at the end of {} years (at maturity) is: {}".format(Time,A))
    
    #plotting the Balance V/S Years graph

    plt.plot(Years,Balance)
    plt.title('Simple Interest Graph (Balance V/S Years')
    plt.xlabel('Years')
    plt.ylabel('Balance')
    plt.show()


    # plotting the SI V/S Years graph

    plt.plot(Years,SI)
    plt.title('Simple Interest Graph (SI V/S Years)')
    plt.xlabel('Years')
    plt.ylabel('Simple Interest')
    plt.show()

    # Plotting the pie chart

    x=[]
    x.append(Deposit)
    x.append(TI)
    x.append(A)
    names=["Deposit","Intrest","Total_Amount"]
    depexplode=[0.2,0.1,0.1]
    plt.pie(x,labels=names,explode=depexplode,autopct='%1.1f%%', shadow=True)
    plt.legend(title="Ratios:")
    plt.show() 








