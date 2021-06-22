from typing import List
import matplotlib.pyplot as plt

def simple_interest(Principle :float,Rate :float,Time: int) ->None:

    """
     Calculates and Visualises Simple Interest

     Parameters:
      Principle(int) : Principle amount
      Rate(float) : Rate of Interest(in percentage)
      Time(int) : Time period(in years)

     Return:
      This function does not return anything.

     Example:
      simple_interest(5000,5.5,5)

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


def compound_interest(P :int,R :float,T :int,freq :str) -> None:
    
    
    """
     Calculates and visualises compound interest 

     Parameters:
        P(float) : Principal amount
        R(float) : Rate of interest (in percentage)
        T(int) : Time
        freq(str) : The frequency in which compound interest should be calculated. 
                    The values can be from the list: ('annually','semiannually','quaterly','monthly')

    Return:
        This function does not return anything.
    
    Example:
       compound_interest(20000,4.5,5,'quaterly')
        
    """


    # defining required lists
    interest : List[float] = []
    time : List[float] = []
    Amount: List[float] = []
    deposit: List[float]=P
    TI : int=0
    fq : int=1
    term : str=' '
    fig, (ax1,ax2)= plt.subplots(2)
    fig.suptitle('Compound Interest')
    
    # compound interest calculation along with graphical representation 
    if(freq=='monthly'):
        fq=12
        term='Month'
    elif (freq == 'annually'):
        fq=1
        term='Year'
    elif (freq == 'quaterly'):
        fq=4
        term='Quarter-Year'
    elif(freq == 'semiannually'):
        fq=2
        term='Semi-Year'
        
    for i in range(fq*T):
        I = P * R/(fq*100)
        P = P + I
        TI+=I
        print("Interest recieved in {} {} is {}".format(term,i+1,I))
        interest.append(I)
        time.append(i+1)
        Amount.append(P)
    print("In {} years you will have {} if interest is compounded {} ".format(T,P,freq))
    ax1.plot(time,Amount)
    ax1.set_xlabel(term)
    ax1.set_ylabel("Amount")
        
        
    x=[]
    x.append(deposit)
    x.append(TI)
    names=["Deposit","Interest"]
    depexplode=[0,0.2]
    ax2.pie(x,labels=names,explode=depexplode , shadow=True)
    ax2.set_title('Ratios')
    plt.tight_layout()
    plt.show() 
