import random

outcomes=[1,2,3,4,5,6]
outcomesdice=["⚀","⚁","⚂","⚃","⚄","⚅"]

print("Do you want to roll a dice?")

ans=str(input())

if ans=="yes":
    chosenOutcome=random.randint(0,5)
    print(outcomesdice[chosenOutcome],outcomes[chosenOutcome])
else:
    print(":(")
    quit()
