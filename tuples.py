import time

elementtuple=("hydrogen","helium","lithium")
elementlist=["hydrogen","helium","lithium"]

print(elementtuple)

elementtuple2=("beryllium","boron","carbon")

print(elementtuple2)

elementtuple3=elementtuple+elementtuple2

print()
print("Now add 'em up!")
print()

print(elementtuple3)

print()
print("Now let's make it a list!")
print()

listoftuple=list(elementtuple3)

print(listoftuple)

print()
print("Now, let's double it!")
print()

print(elementtuple3*2)

print()

if "beryllium" in elementtuple3:
    print("It seems that there is traces of beryllium present.")
    time.sleep(1)
    print("Case closed - it seems Sree Sanka was the public urinator!")

print()
print("Let's convert the list into a tuple!")
print()

tupleoflist=tuple(listoftuple)

print(tupleoflist)


