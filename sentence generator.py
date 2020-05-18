import random
i=random.randint(1,2)
if i==1: h="You "
elif i==2: h="I "
if h=="You ": j="are "
elif h=="I ": j="am "
k=random.randint(1,5)
if i==1: m="me"
elif i==2: m="You"
if k==1: l="yummy."
elif k==2: l="disgusting."
elif k==3: l="a great person."
elif k==4: l="in need of a therapist."
elif k==5: l="dead to "+m+"."
print (h+j+l)
