while 1==1:

    import random

    print("How many times do you want to flip a coin?")


    flips=int(input())

    tails=0
    heads=0


    for tick in range(0,flips):
        coin=random.randint(0,1)
        if coin==0:
            tails=tails+1
        elif coin==1:
            heads=heads+1

    result=100*(tails/flips)
    result2=100*(heads/flips)

    print("Probability of tails:",result,"%")
    print("Probability of heads:",result2,"%")

    print("Would like you like to flip again?")
    ans=str(input())
    if ans=="no":
        exit()
    
    
    
