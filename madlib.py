import random
sentences=random.randint(1,6)

if sentences==1:
    components=["place","past tense verb","name","past tense verb"]
elif sentences==2:
    components=["food","noun","adjective","adjective"]
elif sentences==3:
    components=["eating place","name","adjective","past tense verb"]
elif sentences==4:
    components=["verb","body part","name","verb"]
elif sentences==5:
    components=["noun","adjective","plural noun","superlative adjective"]
elif sentences==6:
    components=["adjective","noun","past tense verb","place"]
    

print(components[0])
input1=input()

print(components[1])
input2=input()    

print(components[2])
input3=input()

print(components[3])
input4=input()

if sentences==1:
    print("I once went to "+input1+". While I was there, I "+input2+". I met a person named "+input3+". He "+input4+".")
elif sentences==2:
    print("I once ate a "+input1+". I ate it with a "+input2+". It tasted very "+input3+". I told the waiter it was "+input4+".")
elif sentences==3:
    print("I was at a "+input1+". I then met my old friend "+input2+". I asked him how he was doing, and he said he was "+input3+" and that he had "+input4+" recently.")
elif sentences==4:
    print("I think I should "+input1+". It would really help my "+input2+". "+input3+" would also really "+input4+" it.")
elif sentences==5:
    print("I really want to practice my "+input1+". It would be really "+input2+". I could show it off to all of my "+input3+". I would be the "+input4+" around.")
elif sentences==6:
    print("I once met a "+input1+" "+input2+". I then "+input3+" off to "+input4+" with "+input2+".")
