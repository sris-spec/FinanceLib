from typing import List
import matplotlib.pyplot as plt
def si(Principle :float,Rate :float,Time: int) ->None:

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
    Years : List[float]=[]
    SI : List[float]=[]
    Balance :List[float] =[]
    # Simple interest calculation along with graphical representation
    Deposit : float =Principle
    TI : float =Principle*Rate*Time/100
    I : float =Principle*Rate/100
    A : float =Principle+TI
    for i in range(Time):
        Principle=Principle+I
        Balance.append(Principle)
        Years.append(i+1)
        SI.append(I)
    print("Amount deposited is:",Deposit)
    print("Intrest earned at the end of each year is:",I)
    print("Total amount at the end of {} years (at maturity) is: {}".format(Time,A))

    #plotting the Balance V/S Years graph
    fig, (ax1,ax2,ax3) = plt.subplots(3)
    fig.suptitle('Simple Interest')
    ax1.plot(Years,Balance,color='#444444', linestyle='-',)
    ax1.legend()
    ax1.set_title('Simple Interest Graph (Balance v/s Years)')
    ax1.set_xlabel('Years')
    ax1.set_ylabel('Balance')

    # plotting the SI V/S Years graph
    ax2.plot(Years,SI,color='#444444', linestyle='--',)
    ax2.legend()
    ax2.set_title('Simple Interest Graph (SI v/s Years)')
    ax2.set_xlabel('Years')
    ax2.set_ylabel('Simple Interest')

    # Plotting the pie chart
    x=[]
    x.append(Deposit)
    x.append(TI)
    x.append(A)
    names=["Deposit","Interest","Total_Amount"]
    depexplode=[0,0,0]
    ax3.pie(x,labels=names,explode=depexplode,autopct='%1.1f%%', shadow=True)
    ax3.set_title('Ratios')

    plt.tight_layout()
    plt.show() 
#si(5000,5.5,5)





