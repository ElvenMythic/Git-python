import random

grocery=[]

grocery.insert(random.randint(0,5),"fibulas")
grocery.insert(random.randint(0,5),"humerus")
grocery.insert(random.randint(0,5),"patels")
grocery.insert(random.randint(0,5),"scapulas")
grocery.insert(random.randint(0,5),"raw cheez-its")
grocery.insert(random.randint(0,5),"egg yolk")

#grocery.append("tacos")

#grocery.append("donuts")

for i in range(0,random.randint(0,5)):
    grocery.pop(random.randint(0,(len(grocery)-1)))

print("The grocery list:",grocery)
