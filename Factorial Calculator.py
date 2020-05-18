def factorial(i):

    inp=i

    if inp==0:
        res=1
    elif inp<0:
        print("Error: factorials of negatives do not exist silly")
    else:
        for tick in range(1,inp):
            inp=inp*tick
        res=inp


while 1==1:
    factorial(int(input()))

    
